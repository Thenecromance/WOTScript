# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyVehicleMarkerViewMeta.py
from gui.Scaleform.framework.entities.View import View

class LobbyVehicleMarkerViewMeta(View):

    def onMarkerClick(self, id):
        self._printOverrideError('onMarkerClick')

    def as_createMarkerS(self, id, vType, vName):
        if self._isDAAPIInited():
            return self.flashObject.as_createMarker(id, vType, vName)

    def as_createPlatoonMarkerS(self, id, vType, pName):
        if self._isDAAPIInited():
            return self.flashObject.as_createPlatoonMarker(id, vType, pName)

    def as_createCustomMarkerS(self, id, icon, text):
        if self._isDAAPIInited():
            return self.flashObject.as_createCustomMarker(id, icon, text)

    def as_removeMarkerS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_removeMarker(id)