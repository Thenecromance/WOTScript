# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventReinforcementPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventReinforcementPanelMeta(BaseDAAPIComponent):

    def as_setPlayerLivesS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerLives(count)