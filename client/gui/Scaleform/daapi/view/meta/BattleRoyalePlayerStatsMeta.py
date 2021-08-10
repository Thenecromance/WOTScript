# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyalePlayerStatsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleRoyalePlayerStatsMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(title)

    def as_setDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(value)