# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehiclePreviewModulesTabMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehiclePreviewModulesTabMeta(BaseDAAPIComponent):

    def setActiveState(self, isActive):
        self._printOverrideError('setActiveState')

    def as_setStatusInfoS(self, message, tooltipId, vehicleType, needToShowAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusInfo(message, tooltipId, vehicleType, needToShowAnim)