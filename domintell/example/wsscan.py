#!/usr/bin/python3
"""
Example code to scan Domintell and return list of installed modules.
Port for WebSockets
:author: ZonderPit <zonderp@milkymail.org>
"""

import time
import logging
import sys
import domintell
from config import host

def _on_message(message):
    print('Received message : ', message)


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
"""
please create a simple credentials.py:
host = {
    'ADDRESS': 'wss://192.168.0.1:17481',
    'USERNAME': '<your login>',
    'SECRET': '<your clear password>'
}
"""

logging.info('Configuring controller for {}'.format(host['ADDRESS']))
controller = domintell.Controller(host['ADDRESS'])

try:
    controller.subscribe(_on_message)

    logging.info('REQUESTSALT')
    controller.requestsalt(host['USERNAME'])

    logging.info('LOGINPSW')
    controller.loginpsw(host['USERNAME'], host['SECRET'])

    logging.info('Starting scan')
    controller.scan(None)

    logging.info('Starting sleep')
    time.sleep(1000)

finally:
    logging.info('Exiting ...')
    controller.stop()
