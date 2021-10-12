# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewBrowseTabMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewBrowseTabMeta(BaseDAAPIComponent):

    def setActiveState(self, isActive):
        self._printOverrideError('setActiveState')

    def onDisclaimerClick(self):
        self._printOverrideError('onDisclaimerClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)