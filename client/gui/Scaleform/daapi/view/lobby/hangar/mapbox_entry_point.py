# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/mapbox_entry_point.py
from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.MapBoxEntryPointMeta import MapBoxEntryPointMeta
from gui.impl.lobby.mapbox.mapbox_entry_point_view import MapBoxEntryPointView

class MapBoxEntryPoint(MapBoxEntryPointMeta):

    def _makeInjectView(self):
        self.__view = MapBoxEntryPointView(ViewFlags.COMPONENT)
        return self.__view