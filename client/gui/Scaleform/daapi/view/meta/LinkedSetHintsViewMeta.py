# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LinkedSetHintsViewMeta.py
from gui.Scaleform.framework.entities.View import View

class LinkedSetHintsViewMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)