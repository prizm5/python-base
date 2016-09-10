#!/usr/bin/python3

import time
import queue
from threading import Thread
from pusher import Pusher
import config
import logging.config
import pusherclient
import json
from pusher import Pusher


logging.config.dictConfig(config.log)
logger = logging.getLogger(__name__)

CLIENT_SECRETS_FILE = "client_secrets.json"

class Plugin():
    def __init__(self, bus):
        self.bus = bus
        with open(CLIENT_SECRETS_FILE) as data_file:    
            data = json.load(data_file)
            
        self.p = pusherclient.Pusher(data['pusher']['key'])
        self.p.connection.bind('pusher:connection_established', self.connect_handler)
        self.p.connect()

    def run(self):
        while True:
            # Do other things in the meantime here...
            time.sleep(1)

    def connect_handler(self, data):
        channel = self.p.subscribe(config.pusher_channel)
        channel.bind('my_event', self.test)

    def simulate_score(self, env):
        data = json.loads(env)
        
    def test(self, env):
        data = json.loads(env)
        self.bus.notify('test',data)

