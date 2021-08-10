# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/historical.py
from regular import RegularAchievement
from mixins import HasVehiclesList, Deprecated

class HistoricalAchievement(Deprecated, HasVehiclesList, RegularAchievement):
    _LIST_NAME = 'vehiclesTakePart'

    def _getVehiclesDescrsList(self):
        return []