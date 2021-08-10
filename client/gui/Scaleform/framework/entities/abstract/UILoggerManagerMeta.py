# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/UILoggerManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class UILoggerManagerMeta(BaseDAAPIComponent):

    def onLog(self, feature, group, action, logLevel, params):
        self._printOverrideError('onLog')