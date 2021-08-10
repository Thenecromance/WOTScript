# Embedded file name: scripts/client/gui/shared/gui_items/customization/__init__.py
from collections import namedtuple
CustomizationTooltipContext = namedtuple('CustomizationTooltipContext', ('itemCD', 'vehicleIntCD', 'showInventoryBlock', 'level', 'showOnlyProgressBlock'))
CustomizationTooltipContext.__new__.__defaults__ = (-1,
 -1,
 False,
 -1,
 False)