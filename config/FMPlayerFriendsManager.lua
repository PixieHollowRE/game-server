OTP_DO_ID_PLAYER_FRIENDS_MANAGER = 4687
OTP_DO_ID_FAIRIES_BADGE_MANAGER = 4690

STATESERVER_OBJECT_UPDATE_FIELD = 2004

FRIEND_ACCEPT_EVENT_ID = 25003

INVRESP_ACCEPTED = 5
INVRESP_DECLINED = 1
INVRESP_ALREADYFRIEND = 4

MAX_FRIENDS = 300

FRIENDMANAGER_ACCOUNT_ONLINE  = 10000
FRIENDMANAGER_ACCOUNT_OFFLINE = 10001

-- DBSS activation (declareObject only; not used for onlineYesNo).
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

CONTEXT = 0
DBSS_QUERY_MAP = {}

-- Account sessions: set on FRIENDMANAGER_ACCOUNT_ONLINE, cleared on OFFLINE.
onlineAccounts = {}

-- Load the TalkFilter
dofile("TalkFilter.lua")

function init(participant)
    participant:subscribeChannel(OTP_DO_ID_PLAYER_FRIENDS_MANAGER)
end

function newInviteTable(inviterId, inviterData, inviteeId, inviteeData)
    return {
        inviterId = inviterId,
        inviterData = inviterData,
        inviteeId = inviteeId,
        inviteeData = inviteeData
    }
end

function applyFriendBadge(participant, avatarId)
    participant:debug(string.format("applyFriendBadge avatarId=%d eventId=%d", avatarId, FRIEND_ACCEPT_EVENT_ID))
    local dg = datagram:new()
    dg:addServerHeader(OTP_DO_ID_FAIRIES_BADGE_MANAGER, OTP_DO_ID_FAIRIES_BADGE_MANAGER, STATESERVER_OBJECT_UPDATE_FIELD)
    dg:addUint32(OTP_DO_ID_FAIRIES_BADGE_MANAGER)
    participant:packFieldToDatagram(dg, "FairiesBadgeManager", "accumulate", {avatarId, FRIEND_ACCEPT_EVENT_ID, 1}, true)
    participant:routeDatagram(dg)
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

function retrieveFairy(data)
    local connAttempts = 0

    while (connAttempts < 3) do
        local response, error_message = http.get(API_BASE .. "retrieveFairy", {
            query=data,
            headers={
                ["User-Agent"]=USER_AGENT,
                ["Authorization"]=API_TOKEN
            }
        })

        if error_message then
            print(string.format("FMPlayerFriendsManager: retrieveFairy returned an error! \"%s\""), error_message)
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            print(string.format("FMPlayerFriendsManager: retrieveFairy returned %d!, \"%s\""), response.status_code, response.body)
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

    -- TODO: If we're here, then we failed to get valid fairy data. Disconnect here
    -- client:sendDisconnect(CLIENT_DISCONNECT_ACCOUNT_ERROR, "Failed to retrieveFairy.", false)
end

function setFairyData(playToken, data)
    local request = {playToken = urlencode(playToken), fieldData = data}
    local json = require("json")
    local result, err = json.encode(request)

    if err then
        print(err)
        print(string.format("FMPlayerFriendsManager: setFairyData encode failed for %s", playToken))
        return false
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
            print(string.format("FMPlayerFriendsManager: setFairyData returned an error! \"%s\"", error_message))
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            print(string.format("FMPlayerFriendsManager: setFairyData returned %d!, \"%s\"", response.status_code, response.body))
            connAttempts = connAttempts + 1
            goto retry
        end

        do
            print(string.format(
                "FMPlayerFriendsManager: setFairyData ok playToken=%s fields=%s",
                playToken,
                json.encode(data)
            ))
            return true
        end

        ::retry::
    end

    print(string.format("FMPlayerFriendsManager: setFairyData failed after retries for %s", playToken))
    return false
end

function friendListContains(friends, accountId)
    if friends == nil then
        return false
    end

    for _, friendId in ipairs(friends) do
        if friendId == accountId then
            return true
        end
    end

    return false
end

function clearInvite(invite)
    if invite == nil then
        return
    end
    invitesByInviterId[invite.inviterId] = nil
    invitesByInviteeId[invite.inviteeId] = nil
end

function clearInviteForAccounts(inviterId, inviteeId)
    local invite = invitesByInviterId[inviterId]
    if invite ~= nil and invite.inviteeId == inviteeId then
        clearInvite(invite)
        return
    end
    invite = invitesByInviteeId[inviteeId]
    if invite ~= nil and invite.inviterId == inviterId then
        clearInvite(invite)
        return
    end
    invitesByInviterId[inviterId] = nil
    invitesByInviteeId[inviteeId] = nil
end

function buildFriendInfo(avatarData, onlineYesNo)
    return {
        avatarData.name, -- avatarName
        avatarData._id, -- avatarId
        avatarData.ownerAccount, -- playerName
        onlineYesNo, -- onlineYesNo
        0, -- openChatEnabledYesNo
        0, -- openChatFriendshipYesNo
        0, -- wlChatEnabledYesNo
        "Fairies", -- location
        "", -- sublocation
        0  -- timestamp
    }
end

function isAccountOnline(accountId)
    return onlineAccounts[accountId] == true
end

function onlineYesNoForAccount(accountId)
    return isAccountOnline(accountId) and 1 or 0
end

function sendUpdatePlayerFriend(participant, accountId, avatarData, otherAccountId, onlineYesNo)
    participant:sendUpdateToAccountId(accountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
        "FMPlayerFriendsManager", "updatePlayerFriend",
        {otherAccountId, buildFriendInfo(avatarData, onlineYesNo), 0})
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

function handleOnline(participant, accountId)
    participant:debug(string.format("handleOnline - %d", accountId))
    local json = require("json")

    onlineAccounts[accountId] = true

    local account = json.decode(retrieveFairy(string.format("identifier=%d", accountId)))
    -- Tell this account's friends that it went online.
    local friendInfo = buildFriendInfo(account, 1)

    for _, friendId in ipairs(account.friends) do
        participant:sendUpdateToAccountId(friendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "updatePlayerFriend", {accountId, friendInfo, 0})

        local dg = datagram:new()
        participant:addServerHeaderWithAccountId(dg, friendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER, CLIENT_AGENT_DECLARE_OBJECT)
        dg:addUint32(account._id)
        dg:addUint16(AVATAR_CLASS)
        participant:routeDatagram(dg)
    end

    -- Send the friend list to the just logged-in account (online from session registry).
    for _, friendId in ipairs(account.friends) do
        local friendAccount = json.decode(retrieveFairy(string.format("identifier=%d", friendId)))
        local onlineYesNo = onlineYesNoForAccount(friendId)
        participant:debug(string.format("Is friend %d online? %d", friendAccount._id, onlineYesNo))

        sendUpdatePlayerFriend(participant, accountId, friendAccount, friendId, onlineYesNo)

        local dg = datagram:new()
        participant:addServerHeaderWithAccountId(dg, accountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER, CLIENT_AGENT_DECLARE_OBJECT)
        dg:addUint32(friendAccount._id)
        dg:addUint16(AVATAR_CLASS)
        participant:routeDatagram(dg)
    end
end

function handleOffline(participant, accountId)
    participant:debug(string.format("handleOffline - %d", accountId))
    local json = require("json")

    onlineAccounts[accountId] = nil

    local account = json.decode(retrieveFairy(string.format("identifier=%d", accountId)))
    -- Tell this account's friends that it went offline.
    local friendInfo = buildFriendInfo(account, 0)

    for _, friendId in ipairs(account.friends) do
        local friendAccount = json.decode(retrieveFairy(string.format("identifier=%d", friendId)))
        if friendAccount ~= nil then
            undeclareFriend(participant, friendAccount._id, account._id)
        end

        participant:sendUpdateToAccountId(friendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "updatePlayerFriend", {accountId, friendInfo, 0})
    end
end

function handleFMPlayerFriendsManager_requestInvite(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherPlayerId = data[2]
    local secretYesNo = data[3]
    participant:debug(string.format("requestInvite - %d - %d - %d", senderId, otherPlayerId, secretYesNo))

    if senderId == otherPlayerId then
        return
    end

    if invitesByInviteeId[senderId] ~= nil then
        makeFriends(participant, invitesByInviteeId[senderId])
        return
    end

    local json = require("json")
    local inviterData = json.decode(retrieveFairy(string.format("identifier=%d", senderId)))
    local inviteeData = json.decode(retrieveFairy(string.format("identifier=%d", otherPlayerId)))

    if inviterData == nil or inviteeData == nil then
        participant:debug(string.format("requestInvite missing fairy data %d -> %d", senderId, otherPlayerId))
        return
    end

    if inviterData.friends == nil then
        inviterData.friends = {}
    end
    if inviteeData.friends == nil then
        inviteeData.friends = {}
    end

    if friendListContains(inviterData.friends, otherPlayerId)
            and friendListContains(inviteeData.friends, senderId) then
        participant:sendUpdateToAccountId(senderId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "invitationResponse", {otherPlayerId, INVRESP_ALREADYFRIEND, 0})
        return
    end

    local pending = invitesByInviterId[senderId]
    if pending ~= nil then
        if pending.inviteeId == otherPlayerId then
            participant:sendUpdateToAccountId(otherPlayerId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "invitationFrom", {senderId, inviterData.name})
            return
        end
        clearInvite(pending)
    end

    local invite = newInviteTable(senderId, inviterData, otherPlayerId, inviteeData)
    invitesByInviterId[senderId] = invite
    invitesByInviteeId[otherPlayerId] = invite

    participant:sendUpdateToAccountId(otherPlayerId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "invitationFrom", {senderId, inviterData.name})
end

function processInviteDecline(participant, declinerId, inviterId, responseContext)
    clearInviteForAccounts(inviterId, declinerId)
    clearInviteForAccounts(declinerId, inviterId)

    if responseContext == nil or responseContext == 0 then
        responseContext = INVRESP_DECLINED
    end

    participant:sendUpdateToAccountId(inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
        "FMPlayerFriendsManager", "invitationResponse", {declinerId, INVRESP_DECLINED, responseContext})
end

function handleFMPlayerFriendsManager_requestDecline(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherPlayerId = data[2]
    participant:debug(string.format("requestDecline - %d - %d", senderId, otherPlayerId))
    processInviteDecline(participant, senderId, otherPlayerId, INVRESP_DECLINED)
end

function handleFMPlayerFriendsManager_requestDeclineWithReason(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherPlayerId = data[2]
    local reason = data[3]
    participant:debug(string.format("requestDeclineWithReason - %d - %d - %d", senderId, otherPlayerId, reason))
    processInviteDecline(participant, senderId, otherPlayerId, reason)
end

function makeFriends(participant, invite)
    participant:debug(string.format("makeFriends - %d - %d", invite.inviterId, invite.inviteeId))

    if invite.inviterData.friends == nil then
        invite.inviterData.friends = {}
    end
    if invite.inviteeData.friends == nil then
        invite.inviteeData.friends = {}
    end

    local inviterAlreadyFriend = friendListContains(invite.inviterData.friends, invite.inviteeId)
    local inviteeAlreadyFriend = friendListContains(invite.inviteeData.friends, invite.inviterId)
    if inviterAlreadyFriend and inviteeAlreadyFriend then
        participant:debug(string.format(
            "makeFriends already friends %d <-> %d",
            invite.inviterId,
            invite.inviteeId
        ))
        clearInvite(invite)
        participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_ALREADYFRIEND, 0})
        return
    end

    local inviterNeedsAdd = not inviterAlreadyFriend
    local inviteeNeedsAdd = not inviteeAlreadyFriend

    if inviterNeedsAdd and #invite.inviterData.friends >= MAX_FRIENDS then
        clearInvite(invite)
        participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_DECLINED, INVRESP_DECLINED})
        return
    end

    if inviteeNeedsAdd and #invite.inviteeData.friends >= MAX_FRIENDS then
        clearInvite(invite)
        participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_DECLINED, INVRESP_DECLINED})
        return
    end

    local inviterAdded = false
    if inviterNeedsAdd then
        table.insert(invite.inviterData.friends, invite.inviteeId)
        if not setFairyData(invite.inviterData.ownerAccount, {friends = invite.inviterData.friends}) then
            table.remove(invite.inviterData.friends)
            clearInvite(invite)
            participant:debug(string.format(
                "makeFriends aborted inviter setFairyData %d -> %d",
                invite.inviterId,
                invite.inviteeId
            ))
            participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_DECLINED, INVRESP_DECLINED})
            return
        end
        inviterAdded = true
        applyFriendBadge(participant, invite.inviterData._id)
        sendUpdatePlayerFriend(participant, invite.inviterId, invite.inviteeData, invite.inviteeId, onlineYesNoForAccount(invite.inviteeId))
    end

    if inviteeNeedsAdd then
        table.insert(invite.inviteeData.friends, invite.inviterId)
        if not setFairyData(invite.inviteeData.ownerAccount, {friends = invite.inviteeData.friends}) then
            table.remove(invite.inviteeData.friends)
            if inviterAdded then
                for i, friendId in ipairs(invite.inviterData.friends) do
                    if friendId == invite.inviteeId then
                        table.remove(invite.inviterData.friends, i)
                        break
                    end
                end
                setFairyData(invite.inviterData.ownerAccount, {friends = invite.inviterData.friends})
            end
            clearInvite(invite)
            participant:debug(string.format(
                "makeFriends aborted invitee setFairyData %d -> %d (rolled back inviter)",
                invite.inviterId,
                invite.inviteeId
            ))
            participant:sendUpdateToAccountId(invite.inviterId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "invitationResponse", {invite.inviteeId, INVRESP_DECLINED, INVRESP_DECLINED})
            return
        end
        applyFriendBadge(participant, invite.inviteeData._id)
        sendUpdatePlayerFriend(participant, invite.inviteeId, invite.inviterData, invite.inviterId, onlineYesNoForAccount(invite.inviterId))
    end

    clearInvite(invite)
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

function handleFMPlayerFriendsManager_requestRemove(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherAccountId = data[2]

    participant:debug(string.format("requestRemove - %d - %d", senderId, otherAccountId))

    local json = require("json")

    local ourData = json.decode(retrieveFairy(string.format("identifier=%d", senderId)))
    local friendData = json.decode(retrieveFairy(string.format("identifier=%d", otherAccountId)))

    for i, friendId in ipairs(ourData.friends) do
        if friendId == otherAccountId then
            -- Remove from our friends list.
            table.remove(ourData.friends, i)

            -- Update us in the database.
            setFairyData(ourData.ownerAccount, {friends = ourData.friends})

            -- Undeclare the object
            undeclareFriend(participant, ourData._id, friendData._id)

            -- Send a response back to the client indicating we've removed this friend.
            participant:sendUpdateToAccountId(senderId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "removePlayerFriend", {otherAccountId})

            break
        end
    end

    -- Update the other friend's list as well.
    for i, friendId in ipairs(friendData.friends) do
        if friendId == senderId then
            -- Remove from our friends list.
            table.remove(friendData.friends, i)

            -- Update us in the database.
            setFairyData(friendData.ownerAccount, {friends = friendData.friends})

            -- Undeclare the object
            undeclareFriend(participant, friendData._id, ourData._id)

            -- Send a response back to the client indicating we've removed this friend.
            participant:sendUpdateToAccountId(otherAccountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "removePlayerFriend", {senderId})

            break
        end
    end
end
