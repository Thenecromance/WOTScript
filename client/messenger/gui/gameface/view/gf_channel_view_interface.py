# Embedded file name: scripts/client/messenger/gui/gameface/view/gf_channel_view_interface.py


class GFChannelViewInterface(object):

    def onChannelControllerInited(self, channelCtrl):
        pass

    def addMessageToView(self, message, isHistoryMessage = False):
        return False