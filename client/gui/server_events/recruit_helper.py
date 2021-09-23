# Embedded file name: scripts/client/gui/server_events/recruit_helper.py
from constants import ENDLESS_TOKEN_TIME
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from items.tankmen import TankmanDescr, MAX_SKILL_LEVEL
from nations import NONE_INDEX, INDICES, NAMES as NationNames
from items import tankmen, vehicles
from items.components.component_constants import EMPTY_STRING
from items.components import skills_constants
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
from gui.shared.gui_items import Tankman
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS
from gui.Scaleform.locale.QUESTS import QUESTS
from helpers.i18n import makeString as _ms
from account_helpers.AccountSettings import AccountSettings, RECRUIT_NOTIFICATIONS
from soft_exception import SoftException
from shared_utils import first
from .events_helpers import getTankmanRewardQuests

class RecruitSourceID(object):
    TANKWOMAN = 'tankwoman'
    TWITCH_0 = 'twitch0'
    TWITCH_1 = 'twitch1'
    TWITCH_2 = 'twitch2'
    TWITCH_3 = 'twitch3'
    TWITCH_4 = 'twitch4'
    TWITCH_5 = 'twitch5'
    TWITCH_6 = 'twitch6'
    TWITCH_7 = 'twitch7'
    TWITCH_8 = 'twitch8'
    TWITCH_9 = 'twitch9'
    TWITCH_10 = 'twitch10'
    TWITCH_11 = 'twitch11'
    TWITCH_12 = 'twitch12'
    TWITCH_13 = 'twitch13'
    TWITCH_14 = 'twitch14'
    TWITCH_15 = 'twitch15'
    TWITCH_16 = 'twitch16'
    TWITCH_17 = 'twitch17'
    TWITCH_18 = 'twitch18'
    TWITCH_19 = 'twitch19'
    TWITCH_20 = 'twitch20'
    TWITCH_21 = 'twitch21'
    TWITCH_22 = 'twitch22'
    TWITCH_23 = 'twitch23'
    TWITCH_24 = 'twitch24'
    TWITCH_25 = 'twitch25'
    TWITCH_26 = 'twitch26'
    BUFFON = 'buffon'
    LOOTBOX = 'lootbox'
    COMMANDER_MARINA = 'commander_marina'
    COMMANDER_PATRICK = 'commander_patrick'
    EVENTS = (TWITCH_0,
     TWITCH_1,
     TWITCH_2,
     TWITCH_3,
     TWITCH_4,
     TWITCH_5,
     TWITCH_6,
     TWITCH_7,
     TWITCH_8,
     TWITCH_9,
     COMMANDER_MARINA,
     COMMANDER_PATRICK,
     TWITCH_10,
     TWITCH_11,
     TWITCH_12,
     TWITCH_13,
     TWITCH_14,
     TWITCH_15,
     TWITCH_16,
     TWITCH_17,
     TWITCH_18,
     TWITCH_19,
     TWITCH_20,
     TWITCH_21,
     TWITCH_22,
     TWITCH_23,
     TWITCH_24,
     TWITCH_25,
     TWITCH_26)


_NEW_SKILL = 'new_skill'
_BASE_NAME = 'base'
_TANKWOMAN_ROLE_LEVEL = 100
_TANKWOMAN_ICON = 'girl-empty.png'
_TANKMAN_NAME = 'tankman'
_TANKMAN_ICON = 'tankman.png'
_TANKWOMAN_LEARNT_SKILLS = ['brotherhood']
_INCREASE_LIMIT_LOGIN = 5

class _BaseRecruitInfo(object):
    __slots__ = ('_recruitID', '_expiryTime', '_nations', '_learntSkills', '_freeXP', '_roleLevel', '_lastSkillLevel', '_roles', '_firstName', '_lastName', '_icon', '_sourceID', '_isFemale', '_hasNewSkill')

    def __init__(self, recruitID, expiryTime, nations, learntSkills, freeXP, roleLevel, lastSkillLevel, firstName, lastName, roles, icon, sourceID, isFemale, hasNewSkill):
        self._recruitID = recruitID
        self._expiryTime = expiryTime
        self._nations = nations
        self._learntSkills = learntSkills
        self._freeXP = freeXP
        self._roleLevel = roleLevel
        self._lastSkillLevel = lastSkillLevel
        self._firstName = firstName
        self._lastName = lastName
        self._roles = roles
        self._icon = icon
        self._sourceID = sourceID
        self._isFemale = isFemale
        self._hasNewSkill = hasNewSkill

    def __cmp__(self, other):
        return cmp(self.getExpiryTimeStamp(), other.getExpiryTimeStamp())

    def getRecruitID(self):
        return self._recruitID

    def getEventName(self):
        return EMPTY_STRING

    def getLabel(self):
        return EMPTY_STRING

    def getDescription(self):
        return EMPTY_STRING

    def getFirstName(self):
        return self._firstName

    def getLastName(self):
        return self._lastName

    def getRoleLevel(self):
        return self._roleLevel

    def getLearntSkills(self, multiplyNew = False):
        if self._hasNewSkill:
            if multiplyNew:
                skillsCount, _ = self.getNewSkillCount(onlyFull=True)
            else:
                skillsCount = 1
            return self._learntSkills + [_NEW_SKILL] * skillsCount
        return self._learntSkills

    def getLastSkillLevel(self):
        return self._lastSkillLevel

    def getExpiryTime(self):
        if self._expiryTime and self._expiryTime < ENDLESS_TOKEN_TIME:
            return backport.getShortDateFormat(self._expiryTime)
        return ''

    def getExpiryTimeStamp(self):
        return self._expiryTime

    def getSmallIcon(self):
        return self._icon

    def getBigIcon(self):
        return '../maps/icons/tankmen/icons/big/{}'.format(self._icon)

    def getBarracksIcon(self):
        return self._icon

    def getRoles(self):
        return self._roles

    def getNations(self):
        return self._nations

    def getFullUserName(self):
        firstName = self.getFirstName()
        lastName = self.getLastName()
        if not firstName:
            return lastName
        return '{} {}'.format(firstName, lastName)

    def getRankID(self):
        return Tankman.calculateRankID(tankmen.MAX_SKILL_LEVEL, self._freeXP, skills=self._getSkillsForDescr(), freeSkills=self._getFreeSkillsForDescr(), lastSkillLevel=self._lastSkillLevel)

    def getSourceID(self):
        return self._sourceID

    def getSpecialIcon(self):
        icon = '../maps/icons/tankmen/icons/special/{}'.format(self._icon)
        if icon in RES_ICONS.MAPS_ICONS_TANKMEN_ICONS_SPECIAL_ENUM:
            return RES_ICONS.getSpecialIcon(self._icon)
        else:
            return None

    def isFemale(self):
        return self._isFemale

    def getNewSkillCount(self, onlyFull = False):
        if self._hasNewSkill:
            tankman = Tankman.Tankman(self.__makeFakeDescriptor().makeCompactDescr())
            count, lastSkillLevel = tankman.newSkillCount
            if onlyFull and lastSkillLevel != MAX_SKILL_LEVEL:
                count = max(count - 1, 0)
                lastSkillLevel = MAX_SKILL_LEVEL
            return (count, lastSkillLevel)
        return (0, 0)

    def _getSkillsForDescr(self):
        return self._learntSkills

    def _getFreeSkillsForDescr(self):
        return ()

    def __makeFakeDescriptor(self):
        vehType = vehicles.VehicleDescr(typeID=(0, 0)).type
        skills = self._getSkillsForDescr()
        freeSkills = self._getFreeSkillsForDescr()
        tmanDescr = tankmen.TankmanDescr(tankmen.generateCompactDescr(tankmen.generatePassport(vehType.id[0], False), vehType.id[1], vehType.crewRoles[0][0], self._roleLevel, skills=skills, freeSkills=freeSkills, lastSkillLevel=self._lastSkillLevel))
        tmanDescr.addXP(self._freeXP)
        return tmanDescr


class _QuestRecruitInfo(_BaseRecruitInfo):
    __slots__ = ('__operationName',)

    def __init__(self, questID, operationName):
        super(_QuestRecruitInfo, self).__init__(recruitID=questID, expiryTime=0, nations=NationNames, learntSkills=_TANKWOMAN_LEARNT_SKILLS, freeXP=0, roleLevel=_TANKWOMAN_ROLE_LEVEL, lastSkillLevel=0, firstName=_ms(QUESTS.BONUSES_ITEM_TANKWOMAN), lastName=EMPTY_STRING, roles=[], icon=_TANKWOMAN_ICON, sourceID=RecruitSourceID.TANKWOMAN, isFemale=True, hasNewSkill=True)
        self.__operationName = operationName

    def getEventName(self):
        return self.getLabel()

    def getLabel(self):
        return _ms(PERSONAL_MISSIONS.OPERATIONTITLE_TITLE, title=self.__operationName)

    def getDescription(self):
        return _ms(TOOLTIPS.NOTRECRUITEDTANKMAN_TANKWOMAN_DESC)

    def getHowToGetInfo(self):
        return ''

    def getNewSkillCount(self, onlyFull = False):
        if self._hasNewSkill:
            return (1, 0)
        return (0, 0)


class _TokenRecruitInfo(_BaseRecruitInfo):
    __slots__ = ('__isPremium', '__group', '__freeSkills')

    def __init__(self, tokenName, expiryTime, nations, isPremium, group, freeSkills, skills, freeXP, lastSkillLevel, roleLevel, sourceID, roles):
        self.__group = group
        self.__isPremium = isPremium
        self.__freeSkills = freeSkills
        learntSkills = freeSkills + skills
        nationNames = [ NationNames[i] for i in nations ]
        needXP = sum((TankmanDescr.levelUpXpCost(level, len(skills) + 1) for level in xrange(0, tankmen.MAX_SKILL_LEVEL)))
        hasNewSkill = freeXP >= needXP
        nation = nations[0] if nations else NONE_INDEX
        allowedRoles, firstName, lastName, icon, isFemale = self.__parseTankmanData(nation)
        if roles:
            for role in roles:
                if skills_constants.SKILL_NAMES[role] not in allowedRoles:
                    raise SoftException('Requested role (%s) is not in the list of allowed roles (%s)' % (skills_constants.SKILL_NAMES[role], ', '.join(map(str, allowedRoles))))

            allowedRoles = [ skills_constants.SKILL_NAMES[role] for role in roles ]
        super(_TokenRecruitInfo, self).__init__(tokenName, expiryTime, nationNames, learntSkills, freeXP, roleLevel, lastSkillLevel, firstName, lastName, allowedRoles, icon, sourceID, isFemale, hasNewSkill)

    def getEventName(self):
        eventName = TOOLTIPS.getNotRecruitedTankmanEventName(self._sourceID)
        if eventName is not None:
            return eventName
        else:
            return TOOLTIPS.getNotRecruitedTankmanEventName(_BASE_NAME)

    def getLabel(self):
        label = TOOLTIPS.getNotRecruitedTankmanEventLabel(self._sourceID)
        if label is not None:
            return label
        else:
            return TOOLTIPS.getNotRecruitedTankmanEventLabel(_TANKMAN_NAME)

    def getDescription(self):
        description = TOOLTIPS.getNotRecruitedTankmanEventDesc(self._sourceID)
        if description is not None:
            return description
        else:
            return TOOLTIPS.getNotRecruitedTankmanEventDesc(_TANKMAN_NAME)

    def getHowToGetInfo(self):
        sourceID = self._sourceID if TOOLTIPS.hasNotRecruitedTankmanEventGetInfo(self._sourceID) else _TANKMAN_NAME
        return TOOLTIPS.getNotRecruitedTankmanEventGetInfo(sourceID)

    def getFullUserNameByNation(self, nationID = None):
        if nationID is None:
            nationID = self._getDefaultNation()
        _, firstName, lastName, _, _ = self.__parseTankmanData(nationID)
        if not firstName:
            return lastName
        else:
            return '{} {}'.format(firstName, lastName)

    def getIconByNation(self, nationID):
        _, _, _, icon, _ = self.__parseTankmanData(nationID)
        return icon

    def getGroupName(self):
        return self.__group

    def _getDefaultNation(self):
        return INDICES.get(first(self._nations), NONE_INDEX)

    def _getSkillsForDescr(self):
        return [ skill for skill in self._learntSkills if skill not in self.__freeSkills ]

    def _getFreeSkillsForDescr(self):
        return self.__freeSkills

    def __parseTankmanData(self, nationID):
        config = tankmen.getNationGroups(nationID, self.__isPremium)
        found = [ c for c in config.itervalues() if c.name == self.__group ]
        if found:
            nationGroup = found[0]
            firstNamesList = nationGroup.firstNamesList
            lastNamesList = nationGroup.lastNamesList
            iconsList = nationGroup.iconsList
            if not firstNamesList or not lastNamesList or not iconsList:
                return ([],
                 EMPTY_STRING,
                 EMPTY_STRING,
                 EMPTY_STRING,
                 False)
            if len(firstNamesList) > 1 or len(lastNamesList) > 1 or len(iconsList) > 1:
                if nationGroup.isFemales:
                    return (nationGroup.rolesList,
                     _ms(QUESTS.BONUSES_ITEM_TANKWOMAN),
                     EMPTY_STRING,
                     _TANKWOMAN_ICON,
                     nationGroup.isFemales)
                return (nationGroup.rolesList,
                 _ms(QUESTS.BONUSES_ITEM_TANKMAN),
                 EMPTY_STRING,
                 _TANKMAN_ICON,
                 nationGroup.isFemales)
            firstNameId = nationGroup.firstNamesList[0]
            lastNameId = nationGroup.lastNamesList[0]
            iconId = nationGroup.iconsList[0]
            nationConfig = tankmen.getNationConfig(nationID)
            return (nationGroup.rolesList,
             nationConfig.getFirstName(firstNameId),
             nationConfig.getLastName(lastNameId),
             nationConfig.getIcon(iconId),
             nationGroup.isFemales)
        return ([],
         EMPTY_STRING,
         EMPTY_STRING,
         EMPTY_STRING,
         False)


def _getRecruitInfoFromQuest(questID):
    for quest, opName in getTankmanRewardQuests():
        if questID == quest.getID():
            return _QuestRecruitInfo(questID, opName)

    return None


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def _getRecruitInfoFromToken(tokenName, eventsCache = None):
    tokenData = tankmen.getRecruitInfoFromToken(tokenName)
    expiryTime = eventsCache.questsProgress.getTokenExpiryTime(tokenName)
    if tokenData is None:
        return
    else:
        return _TokenRecruitInfo(tokenName, expiryTime, **tokenData)


def _getRecruitUniqueIDs():
    result = []
    for recruitID, count in getRecruitIDs().iteritems():
        result.extend([ str(idx) + recruitID for idx in xrange(count) ])

    return set(result)


def getRecruitInfo(recruitID):
    try:
        questID = int(recruitID)
        return _getRecruitInfoFromQuest(questID)
    except ValueError:
        return _getRecruitInfoFromToken(recruitID)


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def getAllRecruitsInfo(sortByExpireTime = False, eventsCache = None):
    result = []
    for tokenName in eventsCache.questsProgress.getTokenNames():
        info = _getRecruitInfoFromToken(tokenName)
        if info is not None:
            count = eventsCache.questsProgress.getTokenCount(tokenName)
            result.extend([ info for _ in range(count) ])

    if sortByExpireTime:
        result.sort()
    for quest, opName in getTankmanRewardQuests():
        result.append(_QuestRecruitInfo(quest.getID(), opName))

    return result


@dependency.replace_none_kwargs(eventsCache=IEventsCache)
def getRecruitIDs(eventsCache = None):
    result = {}
    for tokenName in eventsCache.questsProgress.getTokenNames():
        info = tankmen.getRecruitInfoFromToken(tokenName)
        if info is not None:
            count = eventsCache.questsProgress.getTokenCount(tokenName)
            result[tokenName] = count

    for quest, _ in getTankmanRewardQuests():
        result[str(quest.getID())] = 1

    return result


def getSourceIdFromQuest(questID):
    sourceID = questID.split(':', 1)[0]
    if sourceID in RecruitSourceID.EVENTS:
        return sourceID
    else:
        return None


def getNewRecruitsCounter():
    previous = AccountSettings.getNotifications(RECRUIT_NOTIFICATIONS)
    current = _getRecruitUniqueIDs()
    return len(current.difference(previous))


def setNewRecruitsVisited():
    AccountSettings.setNotifications(RECRUIT_NOTIFICATIONS, _getRecruitUniqueIDs())