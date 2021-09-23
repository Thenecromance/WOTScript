# Embedded file name: scripts/client/EmptyEntity.py
import BigWorld

class EmptyEntity(BigWorld.Entity):

    def __init__(self):
        super(EmptyEntity, self).__init__()
        self.filter = BigWorld.AvatarFilter()

    def onLeaveWorld(self):
        pass

    def drawEdge(self):
        pass

    def removeEdge(self):
        pass

    def isAlive(self):
        return False