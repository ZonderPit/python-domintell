"""
:author: ZonderPit <zonderp@milkymail.org>
"""
import domintell


class LoginPswRequest(domintell.Command):
    """
        send: LOGINPSW@<login>:<final_hash>
    """
    def __init__(self, login, psw_hash):
        domintell.Command.__init__(self, "_LOGINPSW_", "_LOGINPSW_")
        self._login = login
        self._hash = psw_hash

    def command(self):
        return "LOGINPSW@" + self._login + ":" + self._hash

    def is_binary(self):
        return True

