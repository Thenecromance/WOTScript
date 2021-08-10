# Embedded file name: scripts/client/hangar_selectable_objects/__init__.py
from .interfaces import ISelectableObject, ISelectableLogicCallback
from .hangar_selectable_logic import HangarSelectableLogic
__all__ = ('ISelectableObject', 'ISelectableLogicCallback', 'HangarSelectableLogic')