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
            self.data = json.load(data_file)
            
        # self.log_events = ['people_start_playing', 'people_stop_playing',
        #                   'score_goal', 'win_game', 'set_players',
        #                   'score_reset','set_game_mode','start_game']

        # self.bus.subscribe(self.process_event, thread=True,subscribed_events=self.log_events)
        self.bus.subscribe(self.process_event, thread=True)
    
    def run(self):
        while True:
            time.sleep(1)
        
    def process_event(self, ev):
        if ev.data != None :
            d = ev.data
        else:
            d= {}
        self.pusher = Pusher(
                app_id  = self.data['pusher']['app_id'], 
                key     = self.data['pusher']['key'], 
                secret  = self.data['pusher']['secret'])
        self.pusher.trigger(config.pusher_channel_out, ev.name, d)


