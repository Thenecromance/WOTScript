# Embedded file name: scripts/client/skeletons/map_activities.py


class IMapActivities(object):
    __slots__ = ()

    def start(self, name, targetTime):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def generateOfflineActivities(self, spacePath, usePossibility = True):
        raise NotImplementedError