# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyaleLoadingMeta.py
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading

class BattleRoyaleLoadingMeta(BattleLoading):

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)