# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionDetailsContainerViewMeta.py
from gui.Scaleform.daapi.view.meta.BaseMissionDetailsContainerViewMeta import BaseMissionDetailsContainerViewMeta

class MissionDetailsContainerViewMeta(BaseMissionDetailsContainerViewMeta):

    def onTokenBuyClick(self, tokenId, questId):
        self._printOverrideError('onTokenBuyClick')