# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBossTeleportViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBossTeleportViewMeta(BaseDAAPIComponent):

    def onTeleportPointClick(self, id):
        self._printOverrideError('onTeleportPointClick')

    def onCancel(self):
        self._printOverrideError('onCancel')