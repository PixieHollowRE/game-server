OTP_DO_ID_PLAYER_FRIENDS_MANAGER = 4687

STATESERVER_OBJECT_UPDATE_FIELD = 2004

INVRESP_ACCEPTED = 5
INVRESP_DECLINED = 1
INVRESP_ALREADYFRIEND = 4

MAX_FRIENDS = 300

FRIENDMANAGER_ACCOUNT_ONLINE  = 10000
FRIENDMANAGER_ACCOUNT_OFFLINE = 10001

-- Set on the setTalkAccount "flags" field to tell the client to render an
-- incoming whisper as a "whisper to all friends" instead of a 1:1 whisper.
-- Mirrors FMPlayerFriendsManager.GROUP_WHISPER_MASK in the Flash client.
GROUP_WHISPER_MASK = 8

-- For telling a district/house transfer apart from a real logout (handleOffline).
-- Not used for "is my friend online" any more -- onlineAccounts answers that.
DBSS_OBJECT_GET_ACTIVATED      = 2207
DBSS_OBJECT_GET_ACTIVATED_RESP = 2208

-- For declaring friends.
CLIENT_AGENT_DECLARE_OBJECT   = 3010
CLIENT_AGENT_UNDECLARE_OBJECT = 3011

-- Avatar class to declare.
AVATAR_CLASS = dcFile:getClassByName("DistributedFairyPlayer"):getNumber()

-- Load the configuration varables (see config.example.lua)
dofile("config.lua")

invitesByInviterId = {} -- inviterId: invite
invitesByInviteeId = {} -- inviteeId: invite

-- Cache of each online account's friend account-IDs, so "whisper to all
-- friends" (setTalkAccountGroup) can fan out without a per-message retrieveFairy
-- HTTP/DB round-trip. Populated on login, evicted on logout, and kept current as
-- friends are added/removed. This role is the sole mutator of friends lists, so
-- the cache stays authoritative for online accounts.
friendsByAccountId = {} -- accountId: { friendAccountId, ... }

-- Each online account's avatar doId, captured at login.
--
-- handleOffline needs it to ask the stateserver whether the avatar is still
-- activated, which is the only way to tell a district/house transfer from a real
-- logout. It used to get it from an unconditional fetchAccount -- one blocking
-- HTTP round-trip pulling a ~25KB fairy document -- on EVERY offline event, and
-- then discard that document a few lines later on the transfer path without ever
-- reading it. Transfers are the most frequent event this role handles, so that
-- was the most-repeated blocking call in the file.
--
-- An avatar's doId cannot change while its account is online, so caching it at
-- login is safe. Populated in handleOnline, evicted on confirmed logout.
avatarIdByAccountId = {} -- accountId: avatarId

-- Who is currently logged in. This is the role's single source of truth for
-- online-ness: it drives the online dot in every friends panel (sendFriendsList)
-- and the group-whisper fan-out (setTalkAccountGroup), so those two can no longer
-- disagree the way they did when the panel asked the DBSS instead.
--
-- A fairy re-fires FRIENDMANAGER_ACCOUNT_ONLINE/OFFLINE every time its avatar is
-- torn down on one district AI and re-generated on another -- which happens on
-- every district/house transfer, not just at login/logout (a house is a separate
-- realm AI). Those transfers must NOT surface to friends as a login or logout.
-- We collapse the churn here: ONLINE is only a real login the first time we see
-- an account, and OFFLINE is only a real logout once the avatar's stateserver
-- object has actually deactivated (see handleOffline).
--
-- Safe to treat as complete because these Lua roles live inside otpgo, which is
-- also what clients connect to -- the table cannot be empty while players are
-- still connected, since a restart drops every connection with it.
onlineAccounts = {} -- accountId: true

-- Order-preserving copy of `list` with duplicate ids dropped.
--
-- Friends lists have historically accumulated duplicate entries: makeFriends
-- inserted the other player unconditionally, and a consumed invite could be re-run
-- (see clearInvite). Duplicates are corrosive -- they inflate the MAX_FRIENDS
-- count so a player is told their list is full well before it is, and they used to
-- survive a removal because the remove loop stopped at the first match. Every path
-- that loads a list for mutation runs it through here, so a list that is already
-- corrupt heals itself the next time it's written back.
function dedupeFriends(list)
    local seen = {}
    local out = {}
    for _, id in ipairs(list or {}) do
        if not seen[id] then
            seen[id] = true
            table.insert(out, id)
        end
    end
    return out
end

function containsFriend(list, friendId)
    for _, id in ipairs(list or {}) do
        if id == friendId then
            return true
        end
    end
    return false
end

-- Remove every copy of friendId from list, in place. Returns how many were dropped.
function removeAllFriends(list, friendId)
    local removed = 0
    for i = #list, 1, -1 do
        if list[i] == friendId then
            table.remove(list, i)
            removed = removed + 1
        end
    end
    return removed
end

-- Drop friendId from accountId's cached friends list, if accountId is online.
function removeCachedFriend(accountId, friendId)
    local cached = friendsByAccountId[accountId]
    if cached == nil then
        return
    end
    removeAllFriends(cached, friendId)
end

CONTEXT = 0
DBSS_QUERY_MAP = {}

-- Load the TalkFilter
dofile("TalkFilter.lua")

function init(participant)
    participant:subscribeChannel(OTP_DO_ID_PLAYER_FRIENDS_MANAGER)
end

-- An invite deliberately stores only ids and the inviter's display name. It used
-- to carry a full snapshot of both fairies' documents, and makeFriends wrote that
-- snapshot's friends array straight back to the database on accept -- so an invite
-- that sat in the invitee's dialog for a while reverted BOTH players' lists to
-- however they looked when the invite was sent. makeFriends now re-reads both
-- sides at accept time.
function newInviteTable(inviterId, inviterName, inviteeId)
    return {
        inviterId = inviterId,
        inviterName = inviterName,
        inviteeId = inviteeId
    }
end

-- Drop an invite from both indexes.
--
-- makeFriends never used to do this, so a consumed invite stayed in
-- invitesByInviteeId forever: the invitee's NEXT requestInvite -- to anyone --
-- matched the stale entry at the top of handleFMPlayerFriendsManager_requestInvite
-- and re-ran makeFriends on it, which re-added the old friend as a duplicate,
-- swallowed the invite they actually meant to send, and rolled their friends list
-- back to the snapshot the invite was carrying.
function clearInvite(invite)
    if invite == nil then
        return
    end
    if invitesByInviterId[invite.inviterId] == invite then
        invitesByInviterId[invite.inviterId] = nil
    end
    if invitesByInviteeId[invite.inviteeId] == invite then
        invitesByInviteeId[invite.inviteeId] = nil
    end
end

local http = require("http")

if PRODUCTION_ENABLED then
    API_BASE = "https://pixie-hollow.sunrise.games/fairies/api/internal/"
else
    API_BASE = "http://127.0.0.1/fairies/api/internal/"
end

API_BASE = "https://pixie-hollow.sunrise.games/fairies/api/internal/"

-- TODO: These three functions should be moved to their own
-- Lua role.

function urlencode(str)
  if not str then
    return ""
  end
  str = string.gsub(str, "\n", "\r\n")
  str = string.gsub(str, "([^%w %-%_%.~])", function(c)
    return string.format("%%%02X", string.byte(c))
  end)
  str = string.gsub(str, " ", "+")
  return str
end

function retrieveFairy(participant, data)
    local connAttempts = 0

    while (connAttempts < 3) do
        local response, error_message = http.get(API_BASE .. "retrieveFairy", {
            query=data,
            headers={
                ["User-Agent"]=USER_AGENT,
                ["Authorization"]=API_TOKEN
            }
        })

        -- NB: the arguments belong INSIDE string.format. They used to be passed to
        -- print instead, leaving format with a %s and nothing to fill it, so every
        -- one of these log lines threw -- meaning a failed request never actually
        -- retried, it blew up the handler that was mid-flight.
        if error_message then
            participant:warn(string.format("retrieveFairy returned an error! \"%s\"", error_message))
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            participant:warn(string.format("retrieveFairy returned %d!, \"%s\"", response.status_code, response.body))
            connAttempts = connAttempts + 1
            goto retry
        end

        do
            -- If we're here, then we can return the response body.
            return response.body
        end

        -- retry goto to iterate again if we failed to retrieve our fairy data.
        ::retry::
    end

    -- All three attempts failed. Callers go through fetchAccount, which treats nil
    -- as "unavailable" and skips or aborts rather than throwing.
    participant:error(string.format("retrieveFairy gave up after 3 attempts (%s)", tostring(data)))
    return nil
end

-- Write fields onto ONE fairy document, addressed by its distributed object id.
--
-- This used to address the fairy by playToken (the owner account name), which the
-- API resolves with a findOne on ownerAccount -- unambiguous only while an account
-- owns exactly one fairy. Once an account can own several, that lookup returns an
-- arbitrary one, so a friends-list write could land on a different fairy than the
-- read it was derived from. A fairy's _id is unique, so address by that.
function setFairyData(participant, fairyId, data)
    local request = {fairyId = fairyId, fieldData = data}
    local json = require("json")
    local result, err = json.encode(request)

    if err then
        participant:error(string.format("setFairyData - %d: failed to encode JSON (%s)", fairyId, tostring(err)))
        return nil
    end

    local connAttempts = 0
    while (connAttempts < 3) do
        local response, error_message = http.post(API_BASE .. "setFairyData", {
            body=result,
            headers={
                ["Authorization"]=API_TOKEN,
                ["User-Agent"]=USER_AGENT,
                ["Content-Type"]="application/json"
            }
        })

        if error_message then
            participant:warn(string.format("setFairyData - %d returned an error! \"%s\"", fairyId, error_message))
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            participant:warn(string.format("setFairyData - %d returned %d!, \"%s\"", fairyId, response.status_code, response.body))
            connAttempts = connAttempts + 1
            goto retry
        end

        do
            -- If we're here, then we can return the response.
            return response
        end

        -- retry goto to iterate again if we failed to set our fairy data.
        ::retry::
    end

    participant:error(string.format("setFairyData - %d gave up after 3 attempts; this write was LOST", fairyId))
    return nil
end

-- Fetch an account's fairy document, with its friends list deduped, or nil if it
-- can't be had.
--
-- retrieveFairy returns nil when all three attempts fail, and the API answers a
-- missing or deleted fairy with the JSON literal `false`. Both used to be fed
-- straight into json.decode and then indexed, throwing inside whatever handler was
-- running -- which in handleOnline aborted the login fan-out partway through, so
-- every friend after the bad one silently never reached the client. Callers check
-- for nil and either skip that friend or abort cleanly without a partial write.
function fetchAccount(participant, accountId)
    local body = retrieveFairy(participant, string.format("identifier=%d", accountId))
    if body == nil then
        participant:warn(string.format("fetchAccount - %d: retrieveFairy failed", accountId))
        return nil
    end

    local json = require("json")
    local ok, account = pcall(json.decode, body)
    if not ok or type(account) ~= "table" then
        participant:warn(string.format("fetchAccount - %d: bad response \"%s\"", accountId, tostring(body)))
        return nil
    end

    account.friends = dedupeFriends(account.friends)
    return account
end

-- Fetch friend summaries for many accounts in ONE request. Returns a table keyed
-- by the account id as a STRING (JSON object keys always are), or nil if the whole
-- request failed. An id with no fairy is simply absent from the result.
--
-- handleOnline used to call retrieveFairy once per friend, so a 300-friend login
-- meant 301 sequential blocking HTTP round-trips with this entire role -- invites,
-- whispers, everything -- frozen for the duration. It also gave a single failed
-- request 300 chances to take down the login fan-out.
function fetchAccountSummaries(participant, accountIds)
    if #accountIds == 0 then
        return {}
    end

    local json = require("json")
    local body, err = json.encode({identifiers = accountIds})

    if err then
        participant:error(string.format("fetchAccountSummaries: failed to encode JSON (%s)", tostring(err)))
        return nil
    end

    local connAttempts = 0
    while (connAttempts < 3) do
        local response, error_message = http.post(API_BASE .. "retrieveFairies", {
            body=body,
            headers={
                ["Authorization"]=API_TOKEN,
                ["User-Agent"]=USER_AGENT,
                ["Content-Type"]="application/json"
            }
        })

        if error_message then
            participant:warn(string.format("retrieveFairies returned an error! \"%s\"", error_message))
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            participant:warn(string.format("retrieveFairies returned %d!, \"%s\"", response.status_code, response.body))
            connAttempts = connAttempts + 1
            goto retry
        end

        do
            local ok, summaries = pcall(json.decode, response.body)
            if not ok or type(summaries) ~= "table" then
                participant:warn(string.format("retrieveFairies: bad response \"%s\"", tostring(response.body)))
                return nil
            end
            return summaries
        end

        -- retry goto to iterate again if we failed to retrieve the summaries.
        ::retry::
    end

    participant:error(string.format("retrieveFairies gave up after 3 attempts (%d ids)", #accountIds))
    return nil
end

-- The FriendInfo blob the client's friends panel renders for `account`.
function makeFriendInfo(account, onlineYesNo)
    return {
        account.name, -- avatarName
        account._id, -- avatarId
        account.ownerAccount, -- playerName
        onlineYesNo, -- onlineYesNo
        -- Most of these values appears to be unused.
        0, -- openChatEnabledYesNo
        0, -- openChatFriendshipYesNo
        0, -- wlChatEnabledYesNo
        "Fairies", -- location
        "", -- sublocation
        0  -- timestamp
    }
end

function declareFriend(participant, avatarId, friendId)
    -- Make sure that these are AVATAR ids, not ACCOUNT ids.
    local dg = datagram:new()
    participant:addServerHeaderWithAvatarId(dg, avatarId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER, CLIENT_AGENT_DECLARE_OBJECT)
    dg:addUint32(friendId)
    dg:addUint16(AVATAR_CLASS)
    participant:routeDatagram(dg)
end

function undeclareFriend(participant, avatarId, friendId)
    -- Make sure that these are AVATAR ids, not ACCOUNT ids.
    local dg = datagram:new()
    participant:addServerHeaderWithAvatarId(dg, avatarId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER, CLIENT_AGENT_UNDECLARE_OBJECT)
    dg:addUint32(friendId)
    participant:routeDatagram(dg)
end

function queryDBSS(participant, avatarId, callback)
    DBSS_QUERY_MAP[CONTEXT] = callback

    local dg = datagram:new()
    dg:addServerHeader(avatarId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER, DBSS_OBJECT_GET_ACTIVATED)
    dg:addUint32(CONTEXT)
    dg:addUint32(avatarId)
    participant:routeDatagram(dg)

    CONTEXT = CONTEXT + 1
end

function handleDatagram(participant, msgType, dgi)
    if msgType == STATESERVER_OBJECT_UPDATE_FIELD then
        if dgi:readUint32() == OTP_DO_ID_PLAYER_FRIENDS_MANAGER then
            participant:handleUpdateField(dgi, "FMPlayerFriendsManager")
        end
    elseif msgType == FRIENDMANAGER_ACCOUNT_ONLINE then
        handleOnline(participant, dgi:readUint32())
    elseif msgType == FRIENDMANAGER_ACCOUNT_OFFLINE then
        handleOffline(participant, dgi:readUint32())
    elseif msgType == DBSS_OBJECT_GET_ACTIVATED_RESP then
        local context = dgi:readUint32()
        local doId = dgi:readUint32()
        local activated = dgi:readBool()

        local callback = DBSS_QUERY_MAP[context]
        if callback ~= nil then
            callback(doId, activated)
            DBSS_QUERY_MAP[context] = nil
        else
            participant:warn(string.format("Got GET_ACTIVATED_RESP with unknown context: %d", context))
        end
    end
end

-- Push accountId's entire friends list to their own client.
--
-- The client's friends panel has no "fetch my list" request. It is built purely
-- from these updatePlayerFriend messages and is never re-synced, so anything
-- missed here stays missing for the rest of the session. That costs more than an
-- absent row: the chat log resolves a group whisper's sender name by looking the
-- sender's account id up in the panel's own dictionary (ChatLog ->
-- getDoIdByAccountId -> getFairyName), so a friend missing from the panel makes
-- every group whisper they send arrive with a BLANK NAME and a dead name link.
--
-- Which is why this runs on every ACCOUNT_ONLINE, transfers included: rebuilding
-- the panel is how that drift heals.
function sendFriendsList(participant, accountId, friends)
    local summaries = fetchAccountSummaries(participant, friends)

    if summaries == nil then
        participant:error(string.format(
            "sendFriendsList - %d: could not load friend summaries; panel will be empty this session", accountId))
        return
    end

    for _, friendId in ipairs(friends) do
        -- JSON object keys are strings, so index the map with the id formatted.
        local friend = summaries[string.format("%d", friendId)]

        if friend == nil then
            participant:warn(string.format("sendFriendsList - %d: no fairy record for friend %d", accountId, friendId))
        else
            local dg = datagram:new()
            participant:addServerHeaderWithAccountId(dg, accountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER, CLIENT_AGENT_DECLARE_OBJECT)
            dg:addUint32(friend._id)
            dg:addUint16(AVATAR_CLASS)
            participant:routeDatagram(dg)

            -- onlineAccounts is this role's own view of who is logged in, and it is
            -- already what setTalkAccountGroup trusts to skip offline friends.
            -- Reading it here replaces a per-friend DBSS GET_ACTIVATED round-trip
            -- whose response was the ONLY thing that sent the friend at all -- so a
            -- dropped or never-answered response silently erased that friend from
            -- the panel. It also stops the panel and the group-whisper fan-out from
            -- disagreeing about who is online.
            local onlineYesNo = onlineAccounts[friendId] and 1 or 0

            participant:sendUpdateToAccountId(accountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "updatePlayerFriend",
                {friendId, makeFriendInfo(friend, onlineYesNo), 0})
        end
    end
end

function handleOnline(participant, accountId)
    participant:debug(string.format("handleOnline - %d", accountId))

    -- A fairy re-fires ACCOUNT_ONLINE every time its avatar is torn down on one
    -- district AI and re-generated on another, which is every district/house
    -- transfer and not just login. Only the first one is a real login, and only a
    -- real login should surface to friends as a "came online" alert. Sending the
    -- player their own list, on the other hand, is worth doing every time -- see
    -- sendFriendsList.
    local isNewLogin = not onlineAccounts[accountId]

    -- Mark online before anything that can fail. A player whose panel build errors
    -- is still online, and leaving them out of onlineAccounts would hide them from
    -- their friends' online dots and drop them from every group whisper.
    onlineAccounts[accountId] = true

    -- Everything below needs exactly two things out of the fairy document on a
    -- transfer -- the friends list, to rebuild the panel, and the avatar doId --
    -- and both were cached by the login that started this session. makeFriendInfo
    -- is the only other consumer, the only one that wants name/ownerAccount, and it
    -- runs solely on the isNewLogin path. So a transfer can skip the fetch.
    --
    -- That is worth doing because transfers are the most frequent event this role
    -- sees (every district hop, and a house is a separate realm AI), and this was
    -- the last blocking HTTP call left on that path.
    --
    -- Trusting the cache here is safe because this role is the only writer of a
    -- persisted friends array while the server is up: web-api only ever writes one
    -- through setFairyData, which is this role's own endpoint, and every mutation
    -- site here (makeFriends, requestRemove) updates friendsByAccountId in the same
    -- breath. The db-maintenance scripts are the one other writer and they require
    -- the server stopped.
    --
    -- The cost: a transfer no longer re-reads the list from the database, so if the
    -- cache ever DOES drift it now stays drifted for the rest of the session
    -- instead of self-correcting on the next transfer. Login still reads fresh, so
    -- a relog remains the cure.
    local friends = nil
    local avatarId = nil

    if not isNewLogin then
        friends = friendsByAccountId[accountId]
        avatarId = avatarIdByAccountId[accountId]
    end

    if friends ~= nil and avatarId ~= nil then
        participant:debug(string.format(
            "handleOnline - %d already online; transfer re-generate, resending panel from cache", accountId))
    else
        -- A real login, or a transfer whose cache is missing. Note a new login
        -- always lands here: the cache is only consulted above when this is a
        -- transfer, so login behaviour is unchanged and still reads fresh.
        local account = fetchAccount(participant, accountId)
        if account == nil then
            participant:warn(string.format("handleOnline - %d: could not load account; panel not sent", accountId))
            return
        end

        friends = account.friends
        avatarId = account._id

        -- Cache the friends list for group whispers, and the avatar doId so
        -- handleOffline can tell a transfer from a logout without re-fetching this
        -- document. See avatarIdByAccountId.
        friendsByAccountId[accountId] = friends
        avatarIdByAccountId[accountId] = avatarId

        if not isNewLogin then
            participant:debug(string.format(
                "handleOnline - %d already online; transfer re-generate, cache missing so refetched", accountId))
        else
            -- Tell this account's friends that it came online.
            local friendInfo = makeFriendInfo(account, 1)

            -- ONLINE friends only. Both messages below are addressed to friendId's
            -- account channel, which exists only while that friend has a client
            -- connected; for everyone else they are built, packed, and routed to
            -- the message director purely to be dropped for want of a subscriber.
            -- That waste scaled with a player's TOTAL friend count rather than with
            -- how many friends were actually online, so the fuller a list got the
            -- more of the login was spent talking to nobody. Same fix and same
            -- reasoning as setTalkAccountGroup.
            --
            -- Nothing is lost by skipping an offline friend. Their panel is built
            -- from scratch by their own sendFriendsList when they next log in, and
            -- that reads live onlineAccounts for the dot and issues the declare
            -- itself. Since this role is single-threaded, a friend is either already
            -- in onlineAccounts -- so we do send -- or their handleOnline has yet to
            -- run, in which case it will see us, because onlineAccounts[accountId]
            -- was set above before we got here.
            local sent = 0
            for _, friendId in ipairs(friends) do
                if onlineAccounts[friendId] then
                    participant:sendUpdateToAccountId(friendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                        "FMPlayerFriendsManager", "updatePlayerFriend", {accountId, friendInfo, 0})

                    local dg = datagram:new()
                    participant:addServerHeaderWithAccountId(dg, friendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER, CLIENT_AGENT_DECLARE_OBJECT)
                    dg:addUint32(avatarId)
                    dg:addUint16(AVATAR_CLASS)
                    participant:routeDatagram(dg)
                    sent = sent + 1
                end
            end
            participant:debug(string.format(
                "handleOnline - %d announced to %d/%d friends online", accountId, sent, #friends))
        end
    end

    sendFriendsList(participant, accountId, friends)
end

function handleOffline(participant, accountId)
    participant:debug(string.format("handleOffline - %d", accountId))

    -- The avatar doId, cached at login, so the common case -- a transfer -- costs
    -- no HTTP at all. See avatarIdByAccountId for why that matters.
    local avatarId = avatarIdByAccountId[accountId]

    if avatarId == nil then
        -- Nothing cached: either we never saw this account's handleOnline, or its
        -- fetch failed there. Fall back to asking the API, as this used to do
        -- unconditionally.
        participant:warn(string.format(
            "handleOffline - %d: no cached avatar id; falling back to a fetch", accountId))

        local account = fetchAccount(participant, accountId)
        if account == nil then
            -- We can't tell a transfer from a logout without the avatar id, and we
            -- can't notify anyone either. Clear the online flag anyway: leaving it
            -- set is the worse failure, because handleOnline treats an
            -- already-online account as a transfer and returns without sending ANY
            -- friends, so the player's next login would show an empty panel until
            -- this role restarts.
            participant:warn(string.format("handleOffline - %d: could not load account; clearing online flag", accountId))
            onlineAccounts[accountId] = nil
            friendsByAccountId[accountId] = nil
            return
        end

        avatarId = account._id
    end

    -- A fairy fires OFFLINE every time its avatar is torn down on an AI, which
    -- includes every district/house transfer -- not just logout. Tell the two
    -- apart by asking the stateserver whether the avatar object is still
    -- activated: during a transfer it has already migrated to the new AI and is
    -- still activated, whereas a real logout deactivates it. Only the latter is a
    -- genuine "went offline" that friends should be told about.
    queryDBSS(participant, avatarId, function (doId, activated)
        if activated then
            participant:debug(string.format(
                "handleOffline - %d avatar %d still activated; treating as transfer, not logout",
                accountId, doId))
            return
        end

        participant:debug(string.format("handleOffline - %d confirmed logout", accountId))
        onlineAccounts[accountId] = nil

        -- Only a confirmed logout needs the document, and only for the name and
        -- ownerAccount that go into the push. Fetching it here instead of at the
        -- top is what keeps the transfer path free of HTTP. Read it fresh rather
        -- than caching those two fields at login, so a name changed mid-session
        -- still goes out correctly.
        local account = fetchAccount(participant, accountId)

        if account == nil then
            -- Friends will keep showing this player as online until they relog.
            -- Accepted deliberately: the caches below have to be cleared either
            -- way, or the account is stuck "online" for the lifetime of the role.
            participant:warn(string.format(
                "handleOffline - %d: confirmed logout but could not load account; friends not notified", accountId))
        else
            -- Tell this account's ONLINE friends that it went offline. An offline
            -- friend has no client subscribed to its account channel, so an update
            -- aimed at it is built, packed, and routed only to be dropped -- and
            -- they lose nothing, because their own sendFriendsList reads live
            -- onlineAccounts when they next log in. Same reasoning as
            -- setTalkAccountGroup and the handleOnline fan-out.
            local friendInfo = makeFriendInfo(account, 0)

            local sent = 0
            for _, friendId in ipairs(account.friends) do
                if onlineAccounts[friendId] then
                    participant:sendUpdateToAccountId(friendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                        "FMPlayerFriendsManager", "updatePlayerFriend", {accountId, friendInfo, 0})
                    sent = sent + 1
                end
            end
            participant:debug(string.format(
                "handleOffline - %d announced to %d/%d friends online", accountId, sent, #account.friends))
        end

        -- Drop the cached state now that this account is offline.
        friendsByAccountId[accountId] = nil
        avatarIdByAccountId[accountId] = nil
    end)
end

function handleFMPlayerFriendsManager_requestInvite(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherPlayerId = data[2]
    local secretYesNo = data[3]
    participant:debug(string.format("requestInvite - %d - %d - %d", senderId, otherPlayerId, secretYesNo))

    if senderId == otherPlayerId then
        return
    end

    -- Mutual invite: the other player already invited US, so this request is the
    -- acceptance. Only treat it as one when the pending invite is actually FROM
    -- otherPlayerId. The old check accepted whatever invite happened to be sitting
    -- in invitesByInviteeId[senderId], so inviting C while holding a pending invite
    -- from A friended A instead and dropped the invite to C on the floor.
    local pending = invitesByInviteeId[senderId]
    if pending ~= nil and pending.inviterId == otherPlayerId then
        makeFriends(participant, pending)
        return
    end

    local sender = fetchAccount(participant, senderId)
    if sender == nil then
        participant:warn(string.format("requestInvite - %d: could not load sender; dropping invite", senderId))
        return
    end

    if containsFriend(sender.friends, otherPlayerId) then
        participant:debug(string.format("requestInvite - %d - %d are already friends", senderId, otherPlayerId))
        participant:sendUpdateToAccountId(senderId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "invitationResponse", {otherPlayerId, INVRESP_ALREADYFRIEND, 0})
        return
    end

    -- A player has at most one outstanding invite in each direction. Retire any
    -- previous one through clearInvite: overwriting an index slot in place, as this
    -- used to, strands the invite's OTHER half in the opposite index, leaving a
    -- dangling entry that a later requestInvite would match and re-run.
    clearInvite(invitesByInviterId[senderId])
    clearInvite(invitesByInviteeId[otherPlayerId])

    local invite = newInviteTable(senderId, sender.name, otherPlayerId)
    invitesByInviterId[senderId] = invite
    invitesByInviteeId[otherPlayerId] = invite

    participant:sendUpdateToAccountId(otherPlayerId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "invitationFrom", {senderId, invite.inviterName})
end

function handleFMPlayerFriendsManager_requestDecline(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherPlayerId = data[2]
    participant:debug(string.format("requestDecline - %d - %d", senderId, otherPlayerId))

    -- Clear the specific invite between these two, in whichever direction it runs.
    -- The old cleanup nil'd all four index slots for both players, which also wiped
    -- any UNRELATED invite either of them had open with a third player -- and left
    -- that invite's other half dangling in the opposite index, where it would later
    -- be matched and re-run against stale data.
    local invite = invitesByInviteeId[senderId]
    if invite == nil or invite.inviterId ~= otherPlayerId then
        invite = invitesByInviterId[senderId]
        if invite ~= nil and invite.inviteeId ~= otherPlayerId then
            invite = nil
        end
    end
    clearInvite(invite)

    participant:sendUpdateToAccountId(otherPlayerId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "invitationResponse", {senderId, INVRESP_DECLINED, 0})
end

function makeFriends(participant, invite)
    participant:debug(string.format("makeFriends - %d - %d", invite.inviterId, invite.inviteeId))

    -- Consume the invite up front: whatever the outcome below, it is spent, and
    -- leaving it in the indexes is what let it be replayed later against stale data.
    clearInvite(invite)

    -- Re-read both sides rather than trusting a snapshot taken when the invite was
    -- created. The invite may have sat in the invitee's dialog for a long time, and
    -- writing that snapshot's array back erased every friend either player gained
    -- or dropped in the meantime.
    local inviter = fetchAccount(participant, invite.inviterId)
    local invitee = fetchAccount(participant, invite.inviteeId)

    if inviter == nil or invitee == nil then
        participant:warn(string.format("makeFriends - %d - %d: could not load both accounts; aborting",
            invite.inviterId, invite.inviteeId))
        participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_DECLINED, 0})
        return
    end

    local inviterHas = containsFriend(inviter.friends, invite.inviteeId)
    local inviteeHas = containsFriend(invitee.friends, invite.inviterId)

    -- Already friends on both sides. Re-push each to the other so a client that has
    -- drifted out of sync corrects itself, but do NOT insert a second copy of the
    -- id -- unconditional inserts are where the duplicate entries came from.
    if inviterHas and inviteeHas then
        participant:debug(string.format("makeFriends - %d - %d are already friends", invite.inviterId, invite.inviteeId))
        participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "updatePlayerFriend", {invite.inviteeId, makeFriendInfo(invitee, 1), 0})
        participant:sendUpdateToAccountId(invite.inviteeId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "updatePlayerFriend", {invite.inviterId, makeFriendInfo(inviter, 1), 0})
        participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_ALREADYFRIEND, 0})
        return
    end

    -- Both sides need room before either is written. Checking them independently,
    -- as this used to, creates a one-sided friendship when only one list is full:
    -- the player with room sees a friend whose own list has no matching entry, so
    -- the friendship silently vanishes for one of them on their next login.
    if (not inviterHas and #inviter.friends >= MAX_FRIENDS)
        or (not inviteeHas and #invitee.friends >= MAX_FRIENDS) then
        participant:debug(string.format("makeFriends - %d (%d friends) - %d (%d friends): list full",
            invite.inviterId, #inviter.friends, invite.inviteeId, #invitee.friends))
        participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_DECLINED, 0})
        return
    end

    if not inviterHas then
        table.insert(inviter.friends, invite.inviteeId)
        setFairyData(participant, inviter._id, {friends = inviter.friends})

        -- Keep the group-whisper cache current if the inviter is online. The freshly
        -- read list is authoritative, so replace the cache rather than appending to
        -- whatever it happened to be holding.
        if friendsByAccountId[invite.inviterId] ~= nil then
            friendsByAccountId[invite.inviterId] = inviter.friends
        end
    end

    if not inviteeHas then
        table.insert(invitee.friends, invite.inviterId)
        setFairyData(participant, invitee._id, {friends = invitee.friends})

        -- Keep the group-whisper cache current if the invitee is online.
        if friendsByAccountId[invite.inviteeId] ~= nil then
            friendsByAccountId[invite.inviteeId] = invitee.friends
        end
    end

    participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "updatePlayerFriend", {invite.inviteeId, makeFriendInfo(invitee, 1), 0})
    participant:sendUpdateToAccountId(invite.inviteeId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "updatePlayerFriend", {invite.inviterId, makeFriendInfo(inviter, 1), 0})

    participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_ACCEPTED, 0})
end

function handleFMPlayerFriendsManager_setTalkAccount(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherAccountId = data[1]
    participant:debug(string.format("setTalkAccount - %d - %d", senderId, otherAccountId))

    local message = data[4] --chat

    if message == "" then
        return
    end

    local cleanMessage, modifications = filterWhitelist(message, false)

    -- Log it for moderation purposes.
    participant:writeServerEvent("chat-message-whisper", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER, string.format("%d|%d|%s|%s", senderId, otherAccountId, message, cleanMessage))

    participant:sendUpdateToAccountId(otherAccountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "setTalkAccount", {otherAccountId, senderId, data[3], cleanMessage, modifications, 0})
end

function handleFMPlayerFriendsManager_setTalkAccountGroup(participant, fieldId, data)
    -- "Whisper to all friends" (account chat). The client sends this as
    -- setTalkAccountGroup(fromAC, fromName, chat, route_flags, mods, flags),
    -- and we fan it out to every friend as an ordinary setTalkAccount, with the
    -- GROUP_WHISPER_MASK flag set so their client renders it as a group whisper.
    -- route_flags (data[4]) is always 1 from the client's "whisper all" button
    -- and is unused here.
    local senderId = participant:getAccountIdFromSender()
    local fromName = data[2]
    local message = data[3]
    participant:debug(string.format("setTalkAccountGroup - %d", senderId))

    if message == "" then
        return
    end

    local cleanMessage, modifications = filterWhitelist(message, false)

    -- Log it for moderation purposes.
    participant:writeServerEvent("chat-message-whisper-group", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER, string.format("%d|%s|%s", senderId, message, cleanMessage))

    -- The sender is online, so their friends list is normally cached (populated
    -- by handleOnline). Fall back to a fetch only if it's somehow missing.
    local friends = friendsByAccountId[senderId]
    if friends == nil then
        participant:warn(string.format("setTalkAccountGroup - %d not cached, falling back to retrieveFairy", senderId))
        local account = fetchAccount(participant, senderId)
        if account == nil then
            participant:warn(string.format("setTalkAccountGroup - %d could not be loaded; dropping message", senderId))
            return
        end
        friends = account.friends
    end

    -- Echo the message back to the sender so it appears in their own chat.
    -- The client renders this as its own outgoing "to all friends" line only if
    -- it recognizes the fromAC as itself (isThisMyWhisper: fromAC == its dislId).
    -- getAccountIdFromSender() is the account *channel* id, which other players'
    -- friend lists are keyed by, but is NOT the value the client holds as its own
    -- dislId -- so echoing with senderId makes the sender's own message render as
    -- an incoming whisper with a blank name. Use the dislId the client sent for
    -- itself (data[1]) so it self-identifies. The delivery target stays senderId
    -- (the sender's account channel); only the payload identity differs.
    local senderDislId = data[1]
    participant:sendUpdateToAccountId(senderId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "setTalkAccount", {senderDislId, senderDislId, fromName, cleanMessage, modifications, GROUP_WHISPER_MASK})

    -- Broadcast to every ONLINE friend. An offline friend has no client
    -- subscribed to its account channel, so an update aimed at it is built,
    -- packed, and routed to the message director only to be dropped for want of
    -- a subscriber. That wasted work scales with a player's TOTAL friend count,
    -- not with how many friends are actually online -- so players near the
    -- MAX_FRIENDS cap paid the full cost on every group whisper even when almost
    -- all of those friends were offline. (Caching the friends list removed the
    -- per-whisper retrieveFairy round-trip, but not this fan-out cost.)
    --
    -- onlineAccounts is this role's authoritative global view of who is logged
    -- in -- it's a singleton uberdog that sees every ACCOUNT_ONLINE/OFFLINE --
    -- so skipping friends absent from it drops only messages that would have
    -- been discarded anyway.
    --
    -- Send at most ONE copy per recipient, whatever the array holds. A friends
    -- list is supposed to hold each id once, but historically makeFriends
    -- appended unconditionally, so a pair who re-accepted an invite ended up
    -- listed twice and every group whisper reached them twice -- the source of
    -- the "I keep getting the same whisper" reports. makeFriends no longer does
    -- that and db-maintenance/01-dedupe-friends.js cleans the lists already
    -- damaged, but neither makes duplicate DELIVERY impossible; only this does.
    -- The client papers over it up to a point (pushRecvdWhisper drops an
    -- identical whisper once four copies are buffered within 60s), which is why
    -- the symptom read as "a few times" rather than dozens.
    --
    -- Skip the sender too: they already got their echo above, and a list that
    -- somehow names its own owner would otherwise deliver the message twice.
    local sent = 0
    local seen = {[senderId] = true}
    for _, friendId in ipairs(friends) do
        if onlineAccounts[friendId] and not seen[friendId] then
            seen[friendId] = true
            participant:sendUpdateToAccountId(friendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                    "FMPlayerFriendsManager", "setTalkAccount", {friendId, senderId, fromName, cleanMessage, modifications, GROUP_WHISPER_MASK})
            sent = sent + 1
        end
    end
    participant:debug(string.format("setTalkAccountGroup - %d fanned out to %d/%d friends online", senderId, sent, #friends))
end

function handleFMPlayerFriendsManager_requestRemove(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherAccountId = data[2]

    participant:debug(string.format("requestRemove - %d - %d", senderId, otherAccountId))

    local ourData = fetchAccount(participant, senderId)
    local friendData = fetchAccount(participant, otherAccountId)

    if ourData == nil or friendData == nil then
        participant:warn(string.format("requestRemove - %d - %d: could not load both accounts; aborting",
            senderId, otherAccountId))
        return
    end

    -- Strip EVERY copy of the id from both sides. Duplicate entries were possible
    -- (see makeFriends) and the old loops stopped at the first match, so a removed
    -- friend reappeared on the next login.
    if removeAllFriends(ourData.friends, otherAccountId) > 0 then
        setFairyData(participant, ourData._id, {friends = ourData.friends})

        -- Keep the group-whisper cache current if we're online.
        if friendsByAccountId[senderId] ~= nil then
            friendsByAccountId[senderId] = ourData.friends
        end
    end

    -- Update the other friend's list as well.
    if removeAllFriends(friendData.friends, senderId) > 0 then
        setFairyData(participant, friendData._id, {friends = friendData.friends})

        -- Keep the group-whisper cache current if the other account is online.
        if friendsByAccountId[otherAccountId] ~= nil then
            friendsByAccountId[otherAccountId] = friendData.friends
        end
    end

    -- Undeclare the objects
    undeclareFriend(participant, ourData._id, friendData._id)
    undeclareFriend(participant, friendData._id, ourData._id)

    -- Tell both clients unconditionally, even when the id wasn't in the stored list.
    -- The client's panel is built purely from these pushes and is never re-synced,
    -- so skipping the message once the entry was already gone -- which is exactly
    -- what a half-applied removal leaves behind -- stranded the friend on screen
    -- with no way to clear it short of a relog.
    participant:sendUpdateToAccountId(senderId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
        "FMPlayerFriendsManager", "removePlayerFriend", {otherAccountId})
    participant:sendUpdateToAccountId(otherAccountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
        "FMPlayerFriendsManager", "removePlayerFriend", {senderId})
end
