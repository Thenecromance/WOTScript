# Embedded file name: scripts/client_common/script_component/ScriptComponent.py
import BigWorld
from DynamicScriptComponent import DynamicScriptComponent

class ScriptComponent(BigWorld.StaticScriptComponent):

    def __init__(self):
        BigWorld.StaticScriptComponent.__init__(self)