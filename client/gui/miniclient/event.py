# Embedded file name: scripts/client/gui/miniclient/event.py
from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class _DisableEventBoards(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InitEventPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.game_control.event_battles_controller', 'EventBattlesController', 'isEnabled', aspects=(_ParametrizeInitAspect,))


class DisableEventBoards(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'helpers.server_settings', 'ServerSettings', 'isElenEnabled', aspects=(_DisableEventBoards,))