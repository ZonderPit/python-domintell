"""
Salt  Message
:author: ZonderPit <zonderp@milkymail.org>
"""
import json
import domintell
import hashlib
import re


class SaltMessage(domintell.Message):
    """
    Salt message
    """

    def __init__(self, moduleType=None, data=None):
        domintell.Message.__init__(self)
        self._message = ''
        MSG_SALT_INFO = 'INFO:REQUESTSALT:'
        if data[0:len(MSG_SALT_INFO)] == MSG_SALT_INFO:
            self.moduleType = 'SALT_INFO'
            self._message = data

    def populate(self, serialNumber, dataType, dataString):
        pass

    def to_json(self):
        """
        :return: str
        """
        json_dict = self.to_json_basic()
        json_dict['info_message'] = self._message
        return json.dumps(json_dict)

