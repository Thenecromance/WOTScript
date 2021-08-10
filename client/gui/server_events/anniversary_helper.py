# Embedded file name: scripts/client/gui/server_events/anniversary_helper.py
ANNIVERSARY_EVENT_PREFIX = 'anniversary_ga'

def getEventNameByQuest(quest):
    if quest.getID().startswith(ANNIVERSARY_EVENT_PREFIX):
        return ANNIVERSARY_EVENT_PREFIX
    else:
        return None