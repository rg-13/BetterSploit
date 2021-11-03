import configparse
import os
import sys
import time
import random
import requests
import json

from datetime import date, datetime

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)


class TGHunting:
    def __init__(self, api_id, api_hash, phone, username):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.username = username
        self.client = TelegramClient(self.phone, self.api_id, self.api_hash)
        self.client.connect()
        
    def read_config(self):
        config =configparse.ConfigParser()
        config.read('config.ini')
        self.api_id = config['tg_hunting']['api_id']
        self.api_hash = config['tg_hunting']['api_hash']
        self.phone = config['tg_hunting']['phone']
        self.username = config['tg_hunting']['username']
        return self.api_id, self.api_hash, self.phone, self.username

    def random_channel_id(self, start, end):
        return random.choice(range(0, 10))

        
    def json_store_messages(self, messages):
        with open('messages.json', 'w') as f:
            json.dump(messages, f, indent=4)

    def json_store_participants(self, participants):
        with open('participants.json', 'w') as f:
            json.dump(participants, f, indent=4)

    def json_load_messages(self):
        with open('messages.json', 'r') as f:
            messages = json.load(f)
        return messages

    def json_load_participants(self):
        with open('participants.json', 'r') as f:
            participants = json.load(f)
        return participants
    
    def json_search_messages(self, search_string):
        messages = self.json_load_messages()
        for message in messages:
            if search_string in message.message:
                print(message.message)
    


    def tg_connect(self, username, api_id, api_hash):

        username = self.username
        api_id = self.api_id
        api_hash = self.api_hash
        phone = self.phone
        client = self.client
        if not client.is_user_authorized():
            client.send_code_request(phone)
        try:
            client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            password = input('Enter your password: ')
            client.sign_in(password=password)
        print('Connected to Telegram!')

    def tg_get_participants(self, channel_name, limit):
        client = self.client
        if not client.is_user_authorized():
            self.tg_connect()
        else:
            channel_entity = client.get_entity(channel_name)
            if isinstance(channel_entity, PeerChannel):
                participants = client(GetParticipantsRequest(channel_entity, ChannelParticipantsSearch(''), 0, limit,
                                                            filter=ChannelParticipantsSearch('')))
                return participants
                self.json_store_participants(participants.users)
            else:
                print('Channel not found!')
                return None

    def tg_get_participants_count(self, channel_name):
        client = self.client
        if not client.is_user_authorized():
            self.tg_connect()
        else:
            channel_entity = client.get_entity(channel_name)
            if isinstance(channel_entity, PeerChannel):
                participants = client(GetParticipantsRequest(channel_entity, ChannelParticipantsSearch(''), 0, 0,
                                                            filter=ChannelParticipantsSearch('')))
                return participants.total
            else:
                print('Channel not found!')
                return None

    def tg_get_participants_list(self, channel_name, limit):
        client = self.client
        if not client.is_user_authorized():
            self.tg_connect()
        else:
            channel_entity = client.get_entity(channel_name)
            if isinstance(channel_entity, PeerChannel):
                participants = client(GetParticipantsRequest(channel_entity, ChannelParticipantsSearch(''), 0, limit,
                                                            filter=ChannelParticipantsSearch('')))
                return participants.users
                self.json_store_participants(participants.users)
            else:
                print('Channel not found!')
                return None
    
    def tg_get_chat_messages(self, chat_id, limit):
        client = self.client
        if not client.is_user_authorized():
            self.tg_connect()
        else:
            chat_entity = client.get_entity(chat_id)
            if isinstance(chat_entity, PeerChannel):
                messages = client(GetHistoryRequest(chat_entity, 0, limit, 0, 0, 0, 0))
                return messages.messages
                self.json_store_messages(messages.messages)
            else:
                print('Chat not found!')
                return None
    
    def tg_get_random_chat(self, limit):
        client = self.client
        if not client.is_user_authorized():
            self.tg_connect()
        else:
            chats = client.get_dialogs(limit)
            chat_entity = random.choice(chats).entity
            if isinstance(chat_entity, PeerChannel):
                messages = client(GetHistoryRequest(chat_entity, 0, limit, 0, 0, 0, 0))
                return messages.messages
                self.json_store_messages(messages.messages)
            else:
                print('Chat not found!')
                return None

    def tg_stored_messages(self):
        messages = self.json_load_messages()

    def tg_stored_participants(self):
        participants = self.json_load_participants()

    def tg_search_messages(self, search_string):
        messages = self.json_load_messages()
        for message in messages:
            if search_string in message.message:
               return message.message




    def tg_get_random_channel(self, limit):
        client = self.client
        if not client.is_user_authorized():
            self.tg_connect()
        else:
            chats = client.get_dialogs(limit)
            chat_entity = random.choice(chats).entity
            if isinstance(chat_entity, PeerChannel):
                messages = client(GetHistoryRequest(chat_entity, 0, limit, 0, 0, 0, 0))
                return messages.messages
            else:
                print('Channel not found!')
                return None
    
def find_message(search_string):
    messages = TGHunting.tg_stored_messages()
    for message in messages:
        if search_string in message.message:
            return message.message

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    tg_hunting = TGHunting(config)
    tg_hunting.tg_connect()
    tg_hunting.tg_get_random_channel(10)
    tg_hunting.tg_get_random_chat(10)


    if tg_hunting.tg_get_participants_count('@tg_hunting') > 0:
        tg_hunting.tg_get_participants_list('@tg_hunting', 10)
        if find_message('ransomeware'):
            print(tg_hunting.tg_search_messages('ransomeware'))
        else:
            print('No Results.')
    else:
        print('No participants found!')
    

