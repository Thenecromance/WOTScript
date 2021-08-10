# Embedded file name: scripts/client/gui/prb_control/storages/epic_storage.py
from gui.prb_control.storages.local_storage import SessionStorage

class EpicStorage(SessionStorage):

    def _determineSelection(self, arenaVisitor):
        return arenaVisitor.gui.isEpicBattle()