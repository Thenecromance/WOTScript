# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattlePassEntryPointMeta.py
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class BattlePassEntryPointMeta(InjectComponentAdaptor):

    def setIsSmall(self, value):
        self._printOverrideError('setIsSmall')