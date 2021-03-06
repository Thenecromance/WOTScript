# Embedded file name: scripts/client/gui/platform/catalog_service/__init__.py
from controller import PurchaseCache
from skeletons.gui.platform.catalog_service_controller import IPurchaseCache
__all__ = ('getPurchaseCache',)

def getPurchaseCache(manager):
    controller = PurchaseCache()
    controller.init()
    manager.addInstance(IPurchaseCache, controller, finalizer='fini')