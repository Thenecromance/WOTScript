# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/equipment_panel_cmp_tooltips.py
from frameworks.wulf import ViewModel

class EquipmentPanelCmpTooltips(ViewModel):
    __slots__ = ()
    TOOLTIP_SHELL = 'hangarShell'
    TOOLTIP_EQUIPMENT = 'battleRoyaleEquipment'

    def __init__(self, properties = 0, commands = 0):
        super(EquipmentPanelCmpTooltips, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(EquipmentPanelCmpTooltips, self)._initialize()