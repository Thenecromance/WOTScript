# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesIntroMeta.py
from gui.Scaleform.framework.entities.View import View

class RankedBattlesIntroMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onAcceptClick(self):
        self._printOverrideError('onAcceptClick')

    def onDetailedClick(self):
        self._printOverrideError('onDetailedClick')

    def onPlayVideoClick(self):
        self._printOverrideError('onPlayVideoClick')

    def as_setDataS(self, headerData, blocksData):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(headerData, blocksData)