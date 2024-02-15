"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class Ping(domintell.Command):
    """
        send: HELLO message
    """
    def __init__(self):
        domintell.Command.__init__(self)

    def command(self):
        return "HELLO"
