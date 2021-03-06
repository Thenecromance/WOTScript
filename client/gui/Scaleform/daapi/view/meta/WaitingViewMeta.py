# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WaitingViewMeta.py
from gui.Scaleform.framework.entities.View import View

class WaitingViewMeta(View):

    def as_showWaitingS(self, message, softStart):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(message, softStart)

    def as_showBackgroundImgS(self, img):
        if self._isDAAPIInited():
            return self.flashObject.as_showBackgroundImg(img)

    def as_hideWaitingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideWaiting()

    def as_showAwardsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showAwards(value)