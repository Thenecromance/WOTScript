# Embedded file name: scripts/client/gui/shared/utils/requesters/badges_requester.py
import BigWorld
from adisp import async
from gui.doc_loaders.badges_loader import getAvailableBadges
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IBadgesRequester

class BadgesRequester(AbstractSyncDataRequester, IBadgesRequester):

    @property
    def available(self):
        return getAvailableBadges()

    @property
    def selected(self):
        return self.getCacheValue('badges', ())

    @async
    def _requestCache(self, callback):
        BigWorld.player().badges.getCache(lambda resID, value: self._response(resID, value, callback))