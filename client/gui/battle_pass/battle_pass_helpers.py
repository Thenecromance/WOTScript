# Embedded file name: scripts/client/gui/battle_pass/battle_pass_helpers.py
import logging
from collections import namedtuple
import typing
from account_helpers.AccountSettings import AccountSettings, LAST_BATTLE_PASS_POINTS_SEEN
from account_helpers.settings_core.settings_constants import BattlePassStorageKeys
from battle_pass_common import BattlePassState
from constants import ARENA_BONUS_TYPE, QUEUE_TYPE
from gui import GUI_SETTINGS
from gui.Scaleform.genConsts.SKILLS_CONSTANTS import SKILLS_CONSTANTS as SKILLS
from gui.battle_pass.sounds import AwardVideoSoundControl
from gui.impl.gen import R
from gui.prb_control.dispatcher import g_prbLoader
from gui.server_events.recruit_helper import getRecruitInfo
from gui.shared.event_dispatcher import showBattlePassDailyQuestsIntroWindow
from gui.shared.formatters import time_formatters
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency, time_utils
from helpers.dependency import replace_none_kwargs
from nations import INDICES
from shared_utils import first
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.game_control import IBattlePassController
if typing.TYPE_CHECKING:
    from typing import Dict
    from gui.server_events.bonuses import TmanTemplateTokensBonus
_logger = logging.getLogger(__name__)
_CUSTOMIZATION_BONUS_NAME = 'customizations'
_TANKMAN_BONUS_NAME = 'tmanToken'
BattlePassSeasonHistory = namedtuple('BattlePassSeasonHistory', 'maxPostLevel rewardVehicles seasonNum')
TokenPositions = namedtuple('TokenPositions', ['free', 'paid'])

def chaptersIDsComparator(firstID, secondID):
    order = getChaptersOrder()
    return cmp(order.get(firstID), order.get(secondID))


def isBattlePassActiveSeason():
    battlePassController = dependency.instance(IBattlePassController)
    return battlePassController.isVisible()


def getPointsInfoStringID():
    return R.strings.battle_pass.points.top()


def isSeasonEndingSoon():
    battlePassController = dependency.instance(IBattlePassController)
    return battlePassController.getFinalOfferTime() <= time_utils.getServerUTCTime()


def isBattlePassBought():
    battlePassController = dependency.instance(IBattlePassController)
    return battlePassController.isBought()


def getFormattedTimeLeft(seconds):
    return time_formatters.getTillTimeByResource(seconds, R.strings.battle_pass.status.timeLeft, removeLeadingZeros=True)


def getSeasonHistory(seasonID):
    battlePassController = dependency.instance(IBattlePassController)
    seasonsHistory = battlePassController.getSeasonsHistory()
    prevSeasonHistory = seasonsHistory.get(seasonID)
    if prevSeasonHistory is None:
        return
    else:
        return BattlePassSeasonHistory(prevSeasonHistory.get('maxPostLevel'), prevSeasonHistory.get('rewardVehicles'), prevSeasonHistory.get('seasonNum'))


def getLevelFromStats(seasonStats, seasonHistory):
    if seasonStats.maxBase == seasonHistory.getMaxChapterLevel(0):
        level = seasonStats.maxPost
        state = BattlePassState.POST
    else:
        level = seasonStats.maxBase
        state = BattlePassState.BASE
    if seasonStats.maxPost >= seasonHistory.maxPostLevel:
        state = BattlePassState.COMPLETED
    return (state, level)


def getInfoPageURL():
    return GUI_SETTINGS.battlePass.get('infoPage')


def getIntroVideoURL():
    return GUI_SETTINGS.battlePass.get('introVideo')


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def getChaptersOrder(battlePass = None):
    return dict(zip(battlePass.getChapterIDs(), GUI_SETTINGS.battlePass.get('chaptersOrder')))


def getSupportedArenaBonusTypeFor(queueType, isInUnit):
    if queueType == QUEUE_TYPE.BATTLE_ROYALE:
        arenaBonusType = ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD if isInUnit else ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO
    else:
        arenaBonusTypeByQueueType = {QUEUE_TYPE.RANDOMS: ARENA_BONUS_TYPE.REGULAR,
         QUEUE_TYPE.RANKED: ARENA_BONUS_TYPE.RANKED,
         QUEUE_TYPE.MAPBOX: ARENA_BONUS_TYPE.MAPBOX,
         QUEUE_TYPE.EPIC: ARENA_BONUS_TYPE.EPIC_BATTLE}
        arenaBonusType = arenaBonusTypeByQueueType.get(queueType, ARENA_BONUS_TYPE.UNKNOWN)
    return arenaBonusType


def getSupportedCurrentArenaBonusType(queueType = None):
    dispatcher = g_prbLoader.getDispatcher()
    isInUnit = False
    if dispatcher:
        state = dispatcher.getFunctionalState()
        isInUnit = state.isInUnit(state.entityTypeID)
        if queueType is None:
            queueType = dispatcher.getEntity().getQueueType()
    return getSupportedArenaBonusTypeFor(queueType, isInUnit)


def showVideo(videoSource, onVideoClosed = None, isAutoClose = False):
    if not videoSource:
        _logger.error('videoSource is not specified!')
        if callable(onVideoClosed):
            onVideoClosed()
        return
    if not videoSource.exists():
        _logger.error('videoSource is invalid!')
        if callable(onVideoClosed):
            onVideoClosed()
        return
    from gui.impl.lobby.video.video_view import VideoViewWindow
    window = VideoViewWindow(videoSource(), onVideoClosed=onVideoClosed, isAutoClose=isAutoClose, soundControl=AwardVideoSoundControl(videoSource()))
    window.load()


@replace_none_kwargs(battlePass=IBattlePassController, c11nService=ICustomizationService)
def getStyleForChapter(chapter, battlePass = None, c11nService = None):
    stylesConfig = battlePass.getStylesConfig()
    if chapter not in stylesConfig:
        _logger.error('Invalid chapterID: %s', chapter)
        return None
    else:
        return c11nService.getItemByID(GUI_ITEM_TYPE.STYLE, stylesConfig[chapter])


@replace_none_kwargs(battlePass=IBattlePassController)
def getStyleInfoForChapter(chapter, battlePass = None):
    style = getStyleForChapter(chapter, battlePass=battlePass)
    if style is not None:
        return (style.intCD, style.getProgressionLevel())
    else:
        return (None, None)


@replace_none_kwargs(settingsCore=ISettingsCore)
def isBattlePassDailyQuestsIntroShown(settingsCore = None):
    return settingsCore.serverSettings.getBPStorage().get(BattlePassStorageKeys.DAILY_QUESTS_INTRO_SHOWN, False)


def showBattlePassDailyQuestsIntro():
    battlePassController = dependency.instance(IBattlePassController)
    if not battlePassController.isActive():
        return
    settingsCore = dependency.instance(ISettingsCore)
    if not isBattlePassDailyQuestsIntroShown(settingsCore=settingsCore):
        showBattlePassDailyQuestsIntroWindow()
        settingsCore.serverSettings.saveInBPStorage({BattlePassStorageKeys.DAILY_QUESTS_INTRO_SHOWN: True})


def getRecruitNation(recruitInfo):
    nation = first(recruitInfo.getNations())
    return INDICES.get(nation, 0)


def getTankmanInfo(bonus):
    if bonus is None:
        return
    elif bonus.getName() != _TANKMAN_BONUS_NAME:
        return
    tmanToken = first(bonus.getValue().keys())
    if tmanToken is None:
        return
    else:
        return getRecruitInfo(tmanToken)


def getDataByTankman(tankman):
    nation = getRecruitNation(tankman)
    iconName = tankman.getIconByNation(nation)
    tankmanName = tankman.getFullUserNameByNation(nation)
    skills = tankman.getLearntSkills()
    newSkillCount, _ = tankman.getNewSkillCount(onlyFull=True)
    if newSkillCount > 0:
        skills += [SKILLS.TYPE_NEW_SKILL] * (newSkillCount - skills.count(SKILLS.TYPE_NEW_SKILL))
    return (iconName, tankmanName, skills)


def getOfferTokenByGift(tokenID):
    return tokenID.replace('_gift', '')


@replace_none_kwargs(settingsCore=ISettingsCore, battlePass=IBattlePassController)
def updateBuyAnimationFlag(chapterID, settingsCore = None, battlePass = None):
    settings = settingsCore.serverSettings
    shownChapters = settings.getBPStorage().get(BattlePassStorageKeys.BUY_ANIMATION_WAS_SHOWN)
    chapter = 1 << battlePass.getChapterIndex(chapterID)
    if _isChapterShown(shownChapters, chapter):
        settings.saveInBPStorage({BattlePassStorageKeys.BUY_ANIMATION_WAS_SHOWN: shownChapters | chapter})
        return True
    return False


@replace_none_kwargs(battlePass=IBattlePassController)
def updateBattlePassVersion(data, battlePass = None):
    version = battlePass.getSeasonNum()
    if data[BattlePassStorageKeys.FLAGS_VERSION] != version:
        _updateClientSettings()
        _updateServerSettings(data, version)
        return True
    return False


def _updateClientSettings():
    AccountSettings.setSettings(LAST_BATTLE_PASS_POINTS_SEEN, {})


def _updateServerSettings(data, version):
    data[BattlePassStorageKeys.INTRO_SHOWN] = False
    data[BattlePassStorageKeys.INTRO_VIDEO_SHOWN] = False
    data[BattlePassStorageKeys.BUY_ANIMATION_WAS_SHOWN] = 0
    data[BattlePassStorageKeys.FLAGS_VERSION] = version


def _isChapterShown(shownChapters, chapter):
    return shownChapters & chapter == 0