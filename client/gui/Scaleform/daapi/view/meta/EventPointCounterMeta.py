# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventPointCounterMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventPointCounterMeta(BaseDAAPIComponent):

    def as_updateCountS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCount(count)