# Embedded file name: scripts/client/gui/wgnc/errors.py
from soft_exception import SoftException

class ParseError(SoftException):
    pass


class ValidationError(SoftException):
    pass