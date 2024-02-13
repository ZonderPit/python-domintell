"""
:author: ZonderPit <zonderp@milkymail.org>
"""
import domintell


class SaltRequest(domintell.Command):
    """
        send: REQUESTSALT@<login>
    """
    def __init__(self, login):
        domintell.Command.__init__(self, "_REQUESTSALT_", "_REQUESTSALT_")
        self._login = login

    def command(self):
        return "REQUESTSALT@" + self._login

    def is_binary(self):
        return True

