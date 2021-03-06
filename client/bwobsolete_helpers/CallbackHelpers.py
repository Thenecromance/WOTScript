# Embedded file name: scripts/client/bwobsolete_helpers/CallbackHelpers.py
import BigWorld

def IgnoreCallbackIfDestroyed(function):

    def checkIfDestroyed(self, *args, **kwargs):
        if not self.isDestroyed:
            return function(self, *args, **kwargs)

    return checkIfDestroyed