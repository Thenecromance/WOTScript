# Embedded file name: scripts/client/gui/battle_results/components/bootcamp.py
from __future__ import absolute_import
import logging
from shared_utils import first
import BigWorld
from bootcamp.Bootcamp import g_bootcamp
from bootcamp.BootcampConstants import BATTLE_STATS_RESULT_FIELDS, BATTLE_STATS_ICONS
from constants import PREMIUM_ENTITLEMENTS, SPA_ATTRS
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from gui.battle_results.components import base
from gui.battle_results.components.common import makeRegularFinishResultLabel
from gui.battle_results.br_constants import PlayerTeamResult
from gui.Scaleform.locale.BOOTCAMP import BOOTCAMP
from helpers.i18n import makeString
from helpers import dependency
from skeletons.gui.game_control import IBootcampController
_logger = logging.getLogger(__name__)
_BG_FOLDER_PATH = '../maps/icons/bootcamp/battle_result/background/'
_BG_IMAGE_FORMATS = {PlayerTeamResult.WIN: 'bcVictoryBg_{0}.png',
 PlayerTeamResult.DEFEAT: 'bcDefeat.png',
 PlayerTeamResult.DRAW: 'bcDraw.png'}
_STAT_ICON_PATH = '../maps/icons/bootcamp/battle_result/{0}.png'
_STAT_ICON_TOOLTIP_PATH = '../maps/icons/bootcamp/battle_result/tooltip/{0}.png'
_PREMIUM_RESOURCES = {PREMIUM_ENTITLEMENTS.BASIC: {'icon': backport.image(R.images.gui.maps.icons.bootcamp.rewards.bcPremium()),
                              'iconTooltip': backport.image(R.images.gui.maps.icons.bootcamp.rewards.tooltips.bcPremium()),
                              'label': backport.text(R.strings.bootcamp.result.award.premium.label()),
                              'description': backport.text(R.strings.bootcamp.result.award.premium.text())},
 PREMIUM_ENTITLEMENTS.PLUS: {'icon': backport.image(R.images.gui.maps.icons.bootcamp.rewards.bcPremiumPlus()),
                             'iconTooltip': backport.image(R.images.gui.maps.icons.bootcamp.rewards.tooltips.bcPremiumPlus()),
                             'label': backport.text(R.strings.bootcamp.result.award.premiumPlus.label()),
                             'description': backport.text(R.strings.bootcamp.result.award.premiumPlus.text())}}

class BackgroundItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        teamResult = reusable.getPersonalTeamResult()
        lessonNum = g_bootcamp.getLessonNum() - 1
        value = _BG_FOLDER_PATH + _BG_IMAGE_FORMATS[teamResult].format(lessonNum)
        return value


class RewardsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        teamResult = reusable.getPersonalTeamResult()
        if teamResult != PlayerTeamResult.WIN:
            return
        bootcampController = dependency.instance(IBootcampController)
        lessonNum = g_bootcamp.getLessonNum()
        lastLessonNum = g_bootcamp.getContextIntParameter('lastLessonNum')
        lessonSpecificExtras = g_bootcamp.getBattleResultsExtra(lessonNum - 1)
        goldPremuimExtras = []
        showPremium = lessonNum == lastLessonNum and bootcampController.needAwarding()
        if showPremium:
            premiumType = g_bootcamp.getPremiumType(lessonNum)
            if premiumType not in _PREMIUM_RESOURCES:
                _logger.error('Premium type %s is not supported or it is not in the bonuses')
            else:
                goldPremuimExtras.append({'id': premiumType,
                 'label': _PREMIUM_RESOURCES[premiumType]['label'],
                 'description': _PREMIUM_RESOURCES[premiumType]['description'],
                 'icon': _PREMIUM_RESOURCES[premiumType]['icon'],
                 'iconTooltip': _PREMIUM_RESOURCES[premiumType]['iconTooltip']})
                goldPremuimExtras.append({'id': 'gold',
                 'label': backport.text(R.strings.bootcamp.message.gold.label()),
                 'description': backport.text(R.strings.bootcamp.message.gold.premiumPlus.text()),
                 'icon': backport.image(R.images.gui.maps.icons.bootcamp.rewards.bcGold()),
                 'iconTooltip': backport.image(R.images.gui.maps.icons.bootcamp.rewards.tooltips.bcGold())})
        self.addNextComponent(base.DirectStatsItem('medals', lessonSpecificExtras['medals']))
        self.addNextComponent(base.DirectStatsItem('ribbons', lessonSpecificExtras['ribbons']))
        self.addNextComponent(base.DirectStatsItem('unlocks', lessonSpecificExtras['unlocks'] + goldPremuimExtras))


class HasUnlocksFlag(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        teamResult = reusable.getPersonalTeamResult()
        if teamResult != PlayerTeamResult.WIN:
            return False
        bootcampController = dependency.instance(IBootcampController)
        lessonNum = g_bootcamp.getLessonNum()
        lastLessonNum = g_bootcamp.getContextIntParameter('lastLessonNum')
        lessonSpecificExtras = g_bootcamp.getBattleResultsExtra(lessonNum - 1)
        showPremium = lessonNum == lastLessonNum and bootcampController.needAwarding()
        val = bool(lessonSpecificExtras['unlocks']) or showPremium
        return val


class StatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        info = reusable.getPersonalVehiclesInfo(result['personal'])
        teamResult = reusable.getPersonalTeamResult()
        if teamResult == PlayerTeamResult.WIN:
            battleStats = g_bootcamp.getBattleStatsLessonWin()
        else:
            battleStats = g_bootcamp.getBattleStatsLessonDefeat()
        for statType in battleStats:
            statFieldName = BATTLE_STATS_RESULT_FIELDS[statType]
            statVal = info.__getattribute__(statFieldName)
            statVal = backport.getIntegralFormat(statVal)
            self.addNextComponent(base.DirectStatsItem('', {'id': statType,
             'label': makeString(BOOTCAMP.battle_result(statType)),
             'description': makeString(BOOTCAMP.battle_result_description(statType)),
             'value': statVal,
             'icon': _STAT_ICON_PATH.format(BATTLE_STATS_ICONS[statType]),
             'iconTooltip': _STAT_ICON_TOOLTIP_PATH.format(BATTLE_STATS_ICONS[statType])}))


class ResultTypeStrItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        teamResult = reusable.getPersonalTeamResult()
        return backport.text(R.strings.bootcamp.resultlabel.dyn(teamResult)())


class FinishReasonStrItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        teamResult = reusable.getPersonalTeamResult()
        val = makeRegularFinishResultLabel(reusable.common.finishReason, teamResult)
        return val


class FinishReasonItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        return reusable.getPersonalTeamResult()


class ShowRewardsFlag(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        credit = reusable.economics.getBaseCreditsRecords().getRecord('credits')
        xp = reusable.economics.getBaseXPRecords().getRecord('xp')
        return credit != 0 or xp != 0


class PlayerResultItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        playerName = record['players'].values()[0]['name']
        itemId, item = first(reusable.personal.getVehicleItemsIterator())
        killerID = record['personal'][itemId]['killerID']
        ctx = {'player': playerName,
         'vehicle': item.userName}
        if killerID == 0:
            return makeHtmlString('html_templates:bootcamp/player_status', 'alive', ctx=ctx)
        if killerID not in record['common']['bots']:
            return makeHtmlString('html_templates:bootcamp/player_status', 'dead', ctx=ctx)
        killerName = record['common']['bots'][killerID][1]
        killerName = makeString('#bootcamp:' + killerName)
        ctx['killer'] = killerName
        return makeHtmlString('html_templates:bootcamp/player_status', 'killed', ctx=ctx)


class VideoButtonsItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        player = BigWorld.player()
        teamResult = reusable.getPersonalTeamResult()
        buttons = g_bootcamp.getInterludeVideoButtons()
        if player.spaFlags.getFlag(SPA_ATTRS.BOOTCAMP_VIDEO_DISABLED) or teamResult != PlayerTeamResult.WIN or not buttons:
            return None
        else:
            return buttons


class CreditsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        intVal = reusable.economics.getBaseCreditsRecords().getRecord('credits')
        strVal = backport.getGoldFormat(intVal)
        self.addNextComponent(base.DirectStatsItem('value', intVal))
        self.addNextComponent(base.DirectStatsItem('str', strVal))


class XPBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        intVal = reusable.economics.getBaseXPRecords().getRecord('xp')
        strVal = backport.getIntegralFormat(intVal)
        self.addNextComponent(base.DirectStatsItem('value', intVal))
        self.addNextComponent(base.DirectStatsItem('str', strVal))