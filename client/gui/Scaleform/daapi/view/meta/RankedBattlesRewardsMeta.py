# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesRewardsMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesRewardsMeta(BaseDAAPIComponent):

    def onTabChanged(self, viewId):
        self._printOverrideError('onTabChanged')

    def as_setTabsDataS(self, tabs):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsData(tabs)