# Embedded file name: scripts/client/AvatarInputHandler/steel_hunter_control_modes.py
from AvatarInputHandler.control_modes import PostMortemControlMode

class SHPostMortemControlMode(PostMortemControlMode):

    def _isPostmortemDelayEnabled(self):
        return False