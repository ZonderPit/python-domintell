"""
:author: ZonderPit <zonderp@milkymail.org>
"""
import domintell
import hashlib

class LoginPswRequest(domintell.Command):
    """
        send: LOGINPSW@<login>:<final_hash>
    """
    def __init__(self, login, password, nonce, salt):
        domintell.Command.__init__(self, "_LOGINPSW_", "_LOGINPSW_")
        self._login = login
        self._hash = _compute_hash(password, nonce, salt)

    def command(self):
        return "LOGINPSW@" + self._login + ":" + self._hash

    def is_binary(self):
        return True


def _compute_hash(password, nonce, salt):
    salted_password = password + salt
    hashed_salted_password = hashlib.sha512(salted_password.encode('UTF-8')).hexdigest()
    hashed_salted_password_with_nonce = hashed_salted_password + nonce
    return hashlib.sha512(hashed_salted_password_with_nonce.encode('UTF-8')).hexdigest()
