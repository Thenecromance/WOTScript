# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesPrimeTimeMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class RankedBattlesPrimeTimeMeta(WrapperViewMeta):

    def closeView(self):
        self._printOverrideError('closeView')

    def apply(self):
        self._printOverrideError('apply')

    def selectServer(self, id):
        self._printOverrideError('selectServer')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_getServersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getServersDP()