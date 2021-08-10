# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleRoyalePageMeta.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class BattleRoyalePageMeta(ClassicPage):

    def as_updateDamageScreenS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDamageScreen(isVisible)