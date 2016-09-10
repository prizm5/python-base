#!/usr/bin/env python3

import config
import logging.config
import sys
import getopt
import os
import time

from main.bus import Bus
from main.plugin_handler import PluginHandler

logging.config.dictConfig(config.log)
logger = logging.getLogger(__name__)

root = os.path.abspath(os.path.dirname(__file__))

bus = Bus()

# Load plugins
PluginHandler(bus)

while True:
    time.sleep(1)