#!/usr/bin/python3

import time
import queue
from threading import Thread
import config
import logging.config
import json
import requests

logging.config.dictConfig(config.log)
logger = logging.getLogger(__name__)

CLIENT_SECRETS_FILE = "client_secrets.json"

class Plugin():
    def __init__(self, bus):
        self.bus = bus
        with open(CLIENT_SECRETS_FILE) as data_file:    
            data = json.load(data_file)
        self.url = data['slack_url']
        fmap = { 'sample-bus-event': lambda d: self.send('event-name', d) }
        self.bus.subscribe_map(fmap, thread=True)

    def run(self):
        while True:
            time.sleep(1)
        
    def send(self, name, event):
        str = "sample message"
        headers = { 'content-type': 'application/json' }
        payload={
            "username":"slack-user",
            "text": str}
        logger.info(payload)
        response = requests.post(self.url, data=json.dumps(payload), headers=headers)