# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleParametersWithHighlightMeta.py
from gui.Scaleform.daapi.view.lobby.hangar.VehicleParameters import VehicleParameters

class VehicleParametersWithHighlightMeta(VehicleParameters):

    def as_showChangesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showChanges()