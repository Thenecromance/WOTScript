# Embedded file name: scripts/client/skeletons/dynamic_objects_cache.py


class IBattleDynamicObjectsCache(object):

    def getConfig(self, arenaType):
        raise NotImplementedError

    def load(self, arenaType):
        raise NotImplementedError

    def unload(self, arenaType):
        raise NotImplementedError