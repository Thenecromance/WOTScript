# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsMapboxViewMeta.py
from gui.Scaleform.daapi.view.meta.MissionsViewBaseMeta import MissionsViewBaseMeta

class MissionsMapboxViewMeta(MissionsViewBaseMeta):

    def as_showViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showView()