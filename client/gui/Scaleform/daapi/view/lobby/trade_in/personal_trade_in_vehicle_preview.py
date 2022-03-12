# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/trade_in/personal_trade_in_vehicle_preview.py
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS

class PersonalTradeInVehiclePreview(VehiclePreview):

    def setBottomPanel(self):
        self.as_setBottomPanelS(VEHPREVIEW_CONSTANTS.BOTTOM_PANEL_TRADE_IN_PERSONAL_LINKAGE)