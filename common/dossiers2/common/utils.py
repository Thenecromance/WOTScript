# Embedded file name: scripts/common/dossiers2/common/utils.py
import dossiers2
import struct
from typing import Iterable, TYPE_CHECKING
from constants import DOSSIER_TYPE
if TYPE_CHECKING:
    from dossiers2.common.DossierDescr import DossierDescr
__DOSSIER_CONSOLE_OUTPUT_FORMAT = '%s\n--------------------\n%s\n===================='

def printAccountDossier(accountDossierDescr):
    printDossierFromDescr(accountDossierDescr, dossiers2.getAccountDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printVehicleDossier(vehicleDossierDescr):
    printDossierFromDescr(vehicleDossierDescr, dossiers2.getVehicleDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printTankmanDossier(tankmanDossierDescr):
    printDossierFromDescr(tankmanDossierDescr, dossiers2.getTankmanDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printRated7x7Dossier(rated7x7DossierDescr):
    printDossierFromDescr(rated7x7DossierDescr, dossiers2.getRated7x7DossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printClubDossier(clubDossierDescr):
    printDossierFromDescr(clubDossierDescr, dossiers2.getClubDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printDossierFromDescr(dossierDescr, dossierGetter, format):
    printDossier(dossierGetter(dossierDescr), format)


def printDossier(dossier, format):
    print '\n'.join(convertDossierToText(format, dossier))


def convertDossierToText(format, dossier):
    return [ format % (block, dossier[block]) for block in dossier._DossierDescr__blocksLayout ]


def getDossierVersion(dossierCompDescr, versionFormat, latestVersion):
    if dossierCompDescr == '':
        return latestVersion
    return struct.unpack_from(versionFormat, dossierCompDescr)[0]