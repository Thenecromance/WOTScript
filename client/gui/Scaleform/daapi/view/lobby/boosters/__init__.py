# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/boosters/__init__.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ScopeTemplates, ComponentSettings

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.boosters.BoostersPanelComponent import BoostersPanelComponent
    return (ComponentSettings(VIEW_ALIAS.BOOSTERS_PANEL, BoostersPanelComponent, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return ()