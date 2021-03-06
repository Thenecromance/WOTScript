# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AnimatedBackgroundScreenMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AnimatedBackgroundScreenMeta(BaseDAAPIComponent):

    def as_setImageDataS(self, backgroundImgPath, fogImgPath, animate):
        if self._isDAAPIInited():
            return self.flashObject.as_setImageData(backgroundImgPath, fogImgPath, animate)