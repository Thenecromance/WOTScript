# Embedded file name: scripts/client/gui/prb_control/entities/ranked/pre_queue/permissions.py
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions

class RankedPermissions(PreQueuePermissions):

    def canCreateSquad(self):
        return False