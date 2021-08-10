# Embedded file name: scripts/client/gui/shared/utils/functions.py
import random
import re
import typing
import ArenaType
import async as future_async
from adisp import async
from gui import GUI_SETTINGS, SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets
from gui.shared.money import Currency
from helpers.i18n import makeString
from ids_generators import SequenceIDGenerator
from items import ITEM_TYPE_INDICES, vehicles as vehs_core
if typing.TYPE_CHECKING:
    from gui.impl.gen_utils import DynAccessor

def rnd_choice(*args):
    args = list(args)
    for _ in xrange(len(args)):
        c = random.choice(args)
        yield c
        args.remove(c)


def rnd_choice_loop(*args):
    args = list(args)
    while True:
        for value in rnd_choice(*args):
            yield value


def clamp(value, minRange, maxRange):
    if value < minRange:
        return minRange
    if value > maxRange:
        return maxRange
    return value


def roundToMinOrZero(value, minValue):
    if value == 0:
        return value
    return max(minValue, value)


def getShortDescr(descr):
    res = re.findall('<shortDesc>(.*?)</shortDesc>', descr)
    if res:
        res_str = res[0]
    else:
        res_str = descr
    return res_str


def stripShortDescrTags(descr):
    return re.sub('<shortDesc>|</shortDesc>', '', descr)


def stripColorTagDescrTags(descr):
    return re.sub('{colorTagOpen}|{colorTagClose}', '', descr)


def stripExpAmountTags(descr):
    return re.sub('{expTagOpen}|{expTagClose}', '', descr)


def stripShortDescr(descr):
    return re.sub('<shortDesc>(.*?)</shortDesc>', '', descr)


def stripAllTags(descr):
    return re.sub('{\\w+Open}|{\\w+Close}', '', descr)


def stripHTMLTags(descr):
    return re.sub('<(.*?)>', '', descr)


def makeTooltip(header = None, body = None, note = None, attention = None):
    res_str = ''
    if header is not None:
        res_str += '{HEADER}%s{/HEADER}' % makeString(header)
    if body is not None:
        res_str += '{BODY}%s{/BODY}' % makeString(body)
    if note is not None:
        res_str += '{NOTE}%s{/NOTE}' % makeString(note)
    if attention is not None:
        res_str += '{ATTENTION}%s{/ATTENTION}' % makeString(attention)
    return res_str


@async
@future_async.async
def checkAmmoLevel(vehicles, callback):
    showAmmoWarning = False
    ammoWarningMessage = 'lowAmmoAutoLoad'
    alternativeAmmoWarningMessage = 'lowAlternativeAmmoAutoLoad'
    for vehicle in vehicles:
        if vehicle.isReadyToFight:
            if vehicle.isAmmoCanSwitch:
                isNotFull, _ = vehicle.isAmmoNotFullInSetups
            else:
                isNotFull = not vehicle.isAmmoFull
            showAmmoWarning = showAmmoWarning or isNotFull
        if showAmmoWarning:
            from gui.impl.dialogs import dialogs
            from gui.impl.dialogs.builders import ResSimpleDialogBuilder
            builder = ResSimpleDialogBuilder()
            msg = alternativeAmmoWarningMessage if vehicle.isAmmoFull else ammoWarningMessage
            builder.setMessagesAndButtons(R.strings.dialogs.dyn(msg), R.strings.dialogs.dyn(ammoWarningMessage))
            builder.setIcon(R.images.gui.maps.icons.tanksetup.warning.ammunition())
            builder.setPreset(DialogPresets.TROPHY_DEVICE_UPGRADE)
            success = yield future_async.await(dialogs.showSimple(builder.buildInLobby()))
            callback(success)
        else:
            callback(True)


def getModuleGoldStatus(price, money):
    currency = Currency.GOLD
    availableForCredits = 1
    availableForGold = 2
    couldBeBought = 0
    if price.credits and price.credits > money.credits:
        currency = Currency.CREDITS
    else:
        couldBeBought |= availableForCredits
    if price.gold and price.gold < money.gold:
        couldBeBought |= availableForGold
    if not couldBeBought:
        return (False, '#menu:moduleFits/%s_error' % currency, '#tooltips:moduleFits/%s_error' % currency)
    return (True, '', '')


def findConflictedEquipments(itemCompactDescr, itemTypeID, vehicle):
    conflictEqs = []
    if itemTypeID != ITEM_TYPE_INDICES['vehicleEngine']:
        return conflictEqs
    oldModule, = vehicle.descriptor.installComponent(itemCompactDescr)
    for equipmentDescr in vehicle.equipments:
        if equipmentDescr:
            equipment = vehs_core.getItemByCompactDescr(equipmentDescr)
            installPossible, _ = equipment.checkCompatibilityWithVehicle(vehicle.descriptor)
            if not installPossible:
                conflictEqs.append(equipment)

    vehicle.descriptor.installComponent(oldModule)
    return conflictEqs


def findConflictedEquipmentForModule(module, vehicle):
    return findConflictedEquipments(module.compactDescr, ITEM_TYPE_INDICES[module.itemTypeName], vehicle)


def getArenaSubTypeID(arenaTypeID):
    return arenaTypeID >> 16


def getArenaSubTypeName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].gameplayName


def getArenaGeomentryName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].geometryName


def getArenaShortName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].name


def getArenaFullName(arenaTypeID):
    arenaType = ArenaType.g_cache[arenaTypeID]
    arenaName = arenaType.name
    if arenaType.gameplayName != 'ctf':
        arenaName = '%s - %s' % (arenaName, backport.text(R.strings.arenas.type.dyn(arenaType.gameplayName).dyn('name')()))
    return arenaName


def getBattleSubTypeWinText(arenaTypeID, teamID):
    root = R.strings.arenas.type.dyn(ArenaType.g_cache[arenaTypeID].gameplayName)
    description = root.dyn('description')
    if not description:
        description = root.dyn('description{}'.format(teamID))
    return backport.text(description())


def getBattleSubTypeBaseNumber(arenaTypeID, team, baseID):
    teamBasePositions = ArenaType.g_cache[arenaTypeID].teamBasePositions
    if len(teamBasePositions) >= team:
        points = teamBasePositions[team - 1]
        if len(points) > 1:
            return ' %d' % (sorted(points.keys()).index(baseID) + 1)
    points = ArenaType.g_cache[arenaTypeID].controlPoints
    if points:
        if len(points) > 1:
            return ' %d' % baseID
    return ''


def isBaseExists(arenaTypeID, team):
    teamBasePositions = ArenaType.g_cache[arenaTypeID].teamBasePositions
    if len(teamBasePositions) >= team:
        points = teamBasePositions[team - 1]
        if points:
            return True
    return False


def isControlPointExists(arenaTypeID):
    controlPoint = ArenaType.g_cache[arenaTypeID].controlPoints
    if controlPoint:
        return True
    return False


def getAbsoluteUrl(url):
    return url.replace('../', 'img://gui/')


def getRelativeUrl(url):
    return url.replace('img://gui', '..')


_viewIdsGen = None

def getViewName(viewAlias, *args):
    l = list(args)
    if viewAlias:
        l.insert(0, viewAlias)
    return '_'.join(map(str, l))


def getUniqueViewName(viewAlias):
    global _viewIdsGen
    if _viewIdsGen is None:
        _viewIdsGen = SequenceIDGenerator()
    return getViewName(viewAlias, _viewIdsGen.nextSequenceID)


def getPostBattleUniqueSubUrl(svrPackedData, clientPackedData):
    return '%s/%s/%s ' % (GUI_SETTINGS.postBattleExchange.url, svrPackedData, clientPackedData)


def parsePostBattleUniqueSubUrl(uniqueSubUrl):
    return uniqueSubUrl.split('/')[1:]


def showSentInviteMessage(user = None):
    if user is not None:
        if user is not None:
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.PREBATTLE_INVITES_SENDINVITE_NAME, type=SystemMessages.SM_TYPE.Information, name=user.getFullName())
        else:
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.PREBATTLE_INVITES_SENDINVITE, type=SystemMessages.SM_TYPE.Information)
    return


def replaceHyphenToUnderscore(text):
    return text.replace('-', '_')


def getVehTypeIconName(vType, isElite = False):
    vType = replaceHyphenToUnderscore(vType)
    if isElite:
        return '{}_elite'.format(vType)
    return vType


def getImageResourceFromPath(path):
    path = path.replace('../', 'gui/')
    path = path.rsplit('.', 1)[0]
    resource = R.images
    for pathItem in path.split('/'):
        resource = resource.dyn(pathItem)

    return resource