# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventBossWidgetMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBossWidgetMeta(BaseDAAPIComponent):

    def as_setWidgetDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setWidgetData(data)

    def as_updateHpS(self, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHp(hpCurrent)

    def as_updateKillsS(self, kills):
        if self._isDAAPIInited():
            return self.flashObject.as_updateKills(kills)

    def as_updateGeneratorsS(self, availableCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGenerators(availableCount)

    def as_updateGeneratorsChargingS(self, totalTime, remainingTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneratorsCharging(totalTime, remainingTime)

    def as_updateDebuffS(self, totalTime, remainingTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDebuff(totalTime, remainingTime)