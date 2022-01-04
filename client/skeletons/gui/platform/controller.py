# Embedded file name: scripts/client/skeletons/gui/platform/controller.py


class IPlatformRequestController(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError