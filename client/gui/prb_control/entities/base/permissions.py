# Embedded file name: scripts/client/gui/prb_control/entities/base/permissions.py


class IPrbPermissions(object):

    def canExitFromQueue(self):
        return True

    def canChangeVehicle(self):
        return True

    def canSendInvite(self):
        return False

    def canCreateSquad(self):
        return False