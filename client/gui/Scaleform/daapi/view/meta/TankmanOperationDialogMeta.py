# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankmanOperationDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class TankmanOperationDialogMeta(SimpleDialog):

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)