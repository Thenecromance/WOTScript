# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/shop_birthday_section_entry_point.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.ShopBirthdaySectionEntryPointMeta import ShopBirthdaySectionEntryPointMeta
from gui.impl.lobby.eleventh_birthday_calendar.shop_birthday_section_entry_point import ShopBirthdaySectionEntryPointView

class ShopBirthdaySectionEntryPoint(ShopBirthdaySectionEntryPointMeta):

    def _makeInjectView(self):
        self.__view = ShopBirthdaySectionEntryPointView(ViewFlags.COMPONENT)
        return self.__view