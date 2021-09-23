# Embedded file name: scripts/client/gui/battle_results/presenter/events/quests.py
import typing
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import ReusableInfo
    from gui.impl.gen.view_models.views.lobby.postbattle.events.base_event_model import BaseEventModel

def getQuestsEvents(tooltipData, reusable, result):
    return ()