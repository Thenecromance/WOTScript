# Embedded file name: scripts/client/frameworks/state_machine/exceptions.py
from soft_exception import SoftException

class NodeError(SoftException):
    pass


class TransitionError(SoftException):
    pass


class StateError(SoftException):
    pass


class StateMachineError(SoftException):
    pass