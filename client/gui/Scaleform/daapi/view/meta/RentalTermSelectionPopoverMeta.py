# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RentalTermSelectionPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class RentalTermSelectionPopoverMeta(SmartPopOverView):

    def selectTerm(self, itemId):
        self._printOverrideError('selectTerm')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)