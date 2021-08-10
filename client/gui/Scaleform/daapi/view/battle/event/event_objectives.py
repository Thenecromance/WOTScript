# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/event_objectives.py
from gui.Scaleform.daapi.view.meta.EventObjectivesMeta import EventObjectivesMeta

class EventObjectivesPanel(EventObjectivesMeta):

    def updateObjectives(self, txt):
        self.as_updateObjectivesS(txt)

    def hide(self):
        self.as_hideS()