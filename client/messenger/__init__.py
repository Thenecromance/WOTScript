# Embedded file name: scripts/client/messenger/__init__.py
from soft_exception import SoftException
from messenger.m_settings import MessengerSettings

class error(SoftException):
    pass


g_settings = MessengerSettings()