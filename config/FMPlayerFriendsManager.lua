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
FRIENDMANAGER_SYNC_FRIENDS    = 10004

-- For declaring friends to a client's session.
CLIENT_AGENT_DECLARE_OBJECT   = 3010
CLIENT_AGENT_UNDECLARE_OBJECT = 3011

-- Avatar class to declare.
AVATAR_CLASS = dcFile:getClassByName("DistributedFairyPlayer"):getNumber()

-- Load the configuration variables (see config.example.lua)
dofile("config.lua")

invitesByInviterId = {} -- inviterId: invite
invitesByInviteeId = {} -- inviteeId: invite

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

function retrieveFairy(data, participant)
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
            if participant ~= nil then
                participant:error(string.format("retrieveFairy returned an error! \"%s\"", error_message))
            end
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            if participant ~= nil then
                participant:error(string.format("retrieveFairy returned %d!, \"%s\"", response.status_code, response.body))
            end
            connAttempts = connAttempts + 1
            goto retry
        end

        do
            return response.body
        end

        ::retry::
    end
end

function setFairyData(playToken, data, participant)
    local request = {playToken = urlencode(playToken), fieldData = data}
    local json = require("json")
    local result, err = json.encode(request)

    if err then
        if participant ~= nil then
            participant:error(string.format("setFairyData encode failed for %s: %s", playToken, err))
        end
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
            if participant ~= nil then
                participant:error(string.format("setFairyData returned an error! \"%s\"", error_message))
            end
            connAttempts = connAttempts + 1
            goto retry
        end

        if response.status_code ~= 200 then
            if participant ~= nil then
                participant:error(string.format("setFairyData returned %d!, \"%s\"", response.status_code, response.body))
            end
            connAttempts = connAttempts + 1
            goto retry
        end

        do
            return true
        end

        ::retry::
    end

    if participant ~= nil then
        participant:error(string.format("setFairyData failed after retries for %s", playToken))
    end
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

function normalizeAccountId(id)
    if id == nil then
        return nil
    end
    return tonumber(id)
end

function sendUpdatePlayerFriend(participant, accountId, avatarData, otherAccountId, onlineYesNo)
    accountId = normalizeAccountId(accountId)
    otherAccountId = normalizeAccountId(otherAccountId)
    if accountId == nil or otherAccountId == nil then
        return
    end

    participant:sendUpdateToAccountId(accountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
        "FMPlayerFriendsManager", "updatePlayerFriend",
        {otherAccountId, buildFriendInfo(avatarData, onlineYesNo), 0})
end

function notifyFriendsPresence(participant, accountId, account, onlineYesNo)
    local json = require("json")
    local friendInfo = buildFriendInfo(account, onlineYesNo)

    for _, friendId in ipairs(account.friends) do
        local normalizedFriendId = normalizeAccountId(friendId)
        if normalizedFriendId == nil then
            participant:warn(string.format("notifyFriendsPresence - skipping non-numeric friend id %s for account %d", tostring(friendId), accountId))
        else
            participant:sendUpdateToAccountId(normalizedFriendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "updatePlayerFriend", {accountId, friendInfo, 0})

            if onlineYesNo == 1 then
                declareFriendAvatar(participant, normalizedFriendId, account._id)
            else
                local friendBody = retrieveFairy(string.format("identifier=%d", normalizedFriendId), participant)
                if friendBody ~= nil then
                    local friendAccount = json.decode(friendBody)
                    if friendAccount ~= nil then
                        undeclareFriend(participant, friendAccount._id, account._id)
                    end
                end
            end
        end
    end
end

function declareFriendAvatar(participant, viewerAccountId, avatarDoId)
    local dg = datagram:new()
    participant:addServerHeaderWithAccountId(dg, viewerAccountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER, CLIENT_AGENT_DECLARE_OBJECT)
    dg:addUint32(avatarDoId)
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

function handleDatagram(participant, msgType, dgi)
    if msgType == STATESERVER_OBJECT_UPDATE_FIELD then
        if dgi:readUint32() == OTP_DO_ID_PLAYER_FRIENDS_MANAGER then
            participant:handleUpdateField(dgi, "FMPlayerFriendsManager")
        end
    elseif msgType == FRIENDMANAGER_ACCOUNT_ONLINE then
        handleOnline(participant, dgi:readUint32())
    elseif msgType == FRIENDMANAGER_ACCOUNT_OFFLINE then
        handleOffline(participant, dgi:readUint32())
    elseif msgType == FRIENDMANAGER_SYNC_FRIENDS then
        syncFriendListToAccount(participant, dgi:readUint32())
    end
end

function syncFriendListToAccount(participant, accountId)
    accountId = normalizeAccountId(accountId)
    if accountId == nil then
        return
    end

    local json = require("json")
    local accountBody = retrieveFairy(string.format("identifier=%d", accountId), participant)
    if accountBody == nil then
        participant:warn(string.format("syncFriendListToAccount - failed to retrieve fairy for account %d", accountId))
        return
    end

    local account = json.decode(accountBody)
    if account == nil then
        participant:warn(string.format("syncFriendListToAccount - invalid fairy JSON for account %d", accountId))
        return
    end

    if account.friends == nil then
        account.friends = {}
    end

    for _, friendId in ipairs(account.friends) do
        local normalizedFriendId = normalizeAccountId(friendId)
        if normalizedFriendId == nil then
            participant:warn(string.format("syncFriendListToAccount - skipping non-numeric friend id %s for account %d", tostring(friendId), accountId))
        else
            local friendBody = retrieveFairy(string.format("identifier=%d", normalizedFriendId), participant)
            if friendBody == nil then
                participant:warn(string.format("syncFriendListToAccount - failed to retrieve friend %d for account %d", normalizedFriendId, accountId))
            else
                local friendAccount = json.decode(friendBody)
                if friendAccount ~= nil then
                    local onlineYesNo = onlineYesNoForAccount(normalizedFriendId)
                    sendUpdatePlayerFriend(participant, accountId, friendAccount, normalizedFriendId, onlineYesNo)
                    if onlineYesNo == 1 then
                        declareFriendAvatar(participant, accountId, friendAccount._id)
                    end
                end
            end
        end
    end
end

function handleOnline(participant, accountId)
    local wasOnline = isAccountOnline(accountId)
    onlineAccounts[accountId] = true

    if wasOnline then
        participant:debug(string.format("handleOnline: account %d already online, skipping fan-out", accountId))
        return
    end

    participant:debug(string.format("handleOnline: account %d session online", accountId))
    participant:writeServerEvent("friend-session-online", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER, string.format("%d", accountId))
    local json = require("json")

    local accountBody = retrieveFairy(string.format("identifier=%d", accountId), participant)
    if accountBody == nil then
        participant:warn(string.format("handleOnline - failed to retrieve fairy for account %d", accountId))
        return
    end

    local account = json.decode(accountBody)
    if account == nil then
        participant:warn(string.format("handleOnline - invalid fairy JSON for account %d", accountId))
        return
    end

    if account.friends == nil then
        account.friends = {}
    end

    -- Tell all friends this account came online (original Disney fan-out).
    -- TODO: See loginAccount auto-select TODO in FairyClient.lua — enter toast still fails on
    -- first login when a friend is already in-world; offline toast + refresh reconnect works.
    notifyFriendsPresence(participant, accountId, account, 1)

    syncFriendListToAccount(participant, accountId)
end

function handleOffline(participant, accountId)
    accountId = normalizeAccountId(accountId)
    if accountId == nil then
        return
    end

    if not isAccountOnline(accountId) then
        participant:debug(string.format("handleOffline: account %d already offline, skipping fan-out", accountId))
        return
    end

    participant:debug(string.format("handleOffline: account %d session offline", accountId))

    -- Clear session state first so a fast reconnect is not blocked.
    onlineAccounts[accountId] = nil

    participant:writeServerEvent("friend-session-offline", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER, string.format("%d", accountId))
    local json = require("json")

    local accountBody = retrieveFairy(string.format("identifier=%d", accountId), participant)
    if accountBody == nil then
        participant:warn(string.format("handleOffline - failed to retrieve fairy for account %d", accountId))
        return
    end

    local account = json.decode(accountBody)
    if account == nil or account.friends == nil then
        return
    end

    -- Tell all friends this account went offline (original Disney fan-out).
    notifyFriendsPresence(participant, accountId, account, 0)
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

    local inviterBody = retrieveFairy(string.format("identifier=%d", senderId), participant)
    local inviteeBody = retrieveFairy(string.format("identifier=%d", otherPlayerId), participant)
    if inviterBody == nil or inviteeBody == nil then
        participant:debug(string.format("requestInvite missing fairy data %d -> %d", senderId, otherPlayerId))
        return
    end

    local inviterData = json.decode(inviterBody)
    local inviteeData = json.decode(inviteeBody)

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
    participant:writeServerEvent("friend-invite", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
        string.format("%d|%d|%d", senderId, otherPlayerId, secretYesNo))
end

function processInviteDecline(participant, declinerId, inviterId, responseContext)
    clearInviteForAccounts(inviterId, declinerId)
    clearInviteForAccounts(declinerId, inviterId)

    if responseContext == nil or responseContext == 0 then
        responseContext = INVRESP_DECLINED
    end

    participant:writeServerEvent("friend-decline", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
        string.format("%d|%d|%d", declinerId, inviterId, responseContext))

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
        if not setFairyData(invite.inviterData.ownerAccount, {friends = invite.inviterData.friends}, participant) then
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
        declareFriendAvatar(participant, invite.inviterId, invite.inviteeData._id)
    end

    if inviteeNeedsAdd then
        table.insert(invite.inviteeData.friends, invite.inviterId)
        if not setFairyData(invite.inviteeData.ownerAccount, {friends = invite.inviteeData.friends}, participant) then
            table.remove(invite.inviteeData.friends)
            if inviterAdded then
                for i, friendId in ipairs(invite.inviterData.friends) do
                    if friendId == invite.inviteeId then
                        table.remove(invite.inviterData.friends, i)
                        break
                    end
                end
                setFairyData(invite.inviterData.ownerAccount, {friends = invite.inviterData.friends}, participant)
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
        declareFriendAvatar(participant, invite.inviteeId, invite.inviterData._id)
    end

    clearInvite(invite)
    participant:writeServerEvent("friend-accept", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
        string.format("%d|%d", invite.inviterId, invite.inviteeId))
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

    local flags = data[6] or 0
    participant:sendUpdateToAccountId(otherAccountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            "FMPlayerFriendsManager", "setTalkAccount", {otherAccountId, senderId, data[3], cleanMessage, modifications, flags})
end

function handleFMPlayerFriendsManager_setTalkAccountGroup(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    participant:debug(string.format("setTalkAccountGroup - sender %d field %s", senderId, tostring(data[1])))

    local message = data[3]
    if message == "" then
        return
    end

    local cleanMessage, modifications = filterWhitelist(message, false)
    if cleanMessage == "" then
        participant:warn(string.format("setTalkAccountGroup - filtered message empty for account %d", senderId))
        return
    end

    local json = require("json")
    local accountBody = retrieveFairy(string.format("identifier=%d", senderId), participant)
    if accountBody == nil then
        participant:warn(string.format("setTalkAccountGroup - failed to retrieve fairy for account %d", senderId))
        return
    end

    local account = json.decode(accountBody)
    if account == nil or account.friends == nil then
        participant:warn(string.format("setTalkAccountGroup - no friends list for account %d", senderId))
        return
    end

    participant:writeServerEvent("chat-message-group-whisper", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER, string.format("%d|%s|%s", senderId, message, cleanMessage))

    local sentCount = 0
    local friendCount = 0
    local skippedSelf = 0
    local offlineFriendIds = {}
    for _, friendId in ipairs(account.friends) do
        friendCount = friendCount + 1
        local normalizedFriendId = tonumber(friendId)
        if normalizedFriendId == nil then
            participant:warn(string.format("setTalkAccountGroup - skipping non-numeric friend id %s for account %d", tostring(friendId), senderId))
        elseif normalizedFriendId == senderId then
            skippedSelf = skippedSelf + 1
        else
            participant:debug(string.format(
                "setTalkAccountGroup - deliver account %d -> friend %d flags=8 msg=%s",
                senderId, normalizedFriendId, cleanMessage))
            participant:sendUpdateToAccountId(normalizedFriendId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "setTalkAccount", {normalizedFriendId, senderId, data[2], cleanMessage, modifications, 8})
            sentCount = sentCount + 1
            if not isAccountOnline(normalizedFriendId) then
                table.insert(offlineFriendIds, normalizedFriendId)
            end
        end
    end

    if sentCount == 0 then
        participant:debug(string.format(
            "setTalkAccountGroup - account %d sent to 0 friends (friends=%d skipped_self=%d)",
            senderId, friendCount, skippedSelf))
    elseif #offlineFriendIds > 0 then
        participant:debug(string.format(
            "setTalkAccountGroup - account %d sent to %d friends (%s not in online registry)",
            senderId, sentCount, table.concat(offlineFriendIds, ",")))
    else
        participant:debug(string.format("setTalkAccountGroup - sent to %d friends for account %d", sentCount, senderId))
    end
end

function handleFMPlayerFriendsManager_requestRemove(participant, fieldId, data)
    local senderId = participant:getAccountIdFromSender()
    local otherAccountId = data[2]

    participant:debug(string.format("requestRemove - %d - %d", senderId, otherAccountId))

    local json = require("json")

    local ourBody = retrieveFairy(string.format("identifier=%d", senderId), participant)
    local friendBody = retrieveFairy(string.format("identifier=%d", otherAccountId), participant)
    if ourBody == nil or friendBody == nil then
        participant:warn(string.format("requestRemove - failed to retrieve fairy data %d -> %d", senderId, otherAccountId))
        return
    end

    local ourData = json.decode(ourBody)
    local friendData = json.decode(friendBody)
    if ourData == nil or friendData == nil or ourData.friends == nil or friendData.friends == nil then
        participant:warn(string.format("requestRemove - missing friends list %d -> %d", senderId, otherAccountId))
        return
    end

    local removed = false

    for i, friendId in ipairs(ourData.friends) do
        if friendId == otherAccountId then
            -- Remove from our friends list.
            table.remove(ourData.friends, i)

            -- Update us in the database.
            setFairyData(ourData.ownerAccount, {friends = ourData.friends}, participant)

            -- Undeclare the object
            undeclareFriend(participant, ourData._id, friendData._id)

            -- Send a response back to the client indicating we've removed this friend.
            participant:sendUpdateToAccountId(senderId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "removePlayerFriend", {otherAccountId})

            removed = true
            break
        end
    end

    -- Update the other friend's list as well.
    for i, friendId in ipairs(friendData.friends) do
        if friendId == senderId then
            -- Remove from our friends list.
            table.remove(friendData.friends, i)

            -- Update us in the database.
            setFairyData(friendData.ownerAccount, {friends = friendData.friends}, participant)

            -- Undeclare the object
            undeclareFriend(participant, friendData._id, ourData._id)

            -- Send a response back to the client indicating we've removed this friend.
            participant:sendUpdateToAccountId(otherAccountId, OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
                "FMPlayerFriendsManager", "removePlayerFriend", {senderId})

            removed = true
            break
        end
    end

    if removed then
        participant:writeServerEvent("friend-remove", "FMPlayerFriendsManager", OTP_DO_ID_PLAYER_FRIENDS_MANAGER,
            string.format("%d|%d", senderId, otherAccountId))
    end
end
