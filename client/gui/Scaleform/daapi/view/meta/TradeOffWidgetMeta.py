# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TradeOffWidgetMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TradeOffWidgetMeta(BaseDAAPIComponent):

    def onClick(self):
        self._printOverrideError('onClick')

    def onResetClick(self):
        self._printOverrideError('onResetClick')

    def getTooltip(self):
        self._printOverrideError('getTooltip')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)