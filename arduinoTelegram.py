import random
import os
import requests
import logging
import json
import serial
import time
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('nbt')
try:
    with open('last_updated.txt', 'r') as f:
        try:
            last_updated = int(f.read())
        except ValueError:
            last_updated = 0
    f.close()
except FileNotFoundError:
    last_updated = 0

skip_list = []
arduino =  serial.Serial("/dev/ttyACM0",9600)


BOT_KEY = ''
API_BASE = 'https://api.telegram.org/bot'

def get_updates():
    log.debug('Checking for requests')
    return json.loads(requests.get(API_BASE + BOT_KEY + '/getUpdates', params = {'offset': last_updated + 1}).text)

def turnOn():
	arduino.write(b"H")

def turnOff():
	arduino.write(b"L")


def sendMessage(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(API_BASE + BOT_KEY + '/sendMessage', data = payload)

if __name__ == '__main__':
    log.debug('Starting up')
    log.debug('Last updated id: {0}'.format(last_updated))
    while (True):
        r = get_updates()
        
        if r['ok']:
            for req in r['result']:
                chat_sender_id = req['message']['chat']['id']
                chat_text = req['message']['text']
                last_updated = req['update_id']
                log.debug('Chat text received: {0}'.format(chat_text))
                if chat_text == '/on':
                    sendMessage(chat_sender_id,turnOn())
                    last_updated = req['update_id']
                if chat_text == '/off':
                	sendMessage(chat_sender_id,turnOff())
                	last_updated = req['update_id']
                	
                if chat_text == '/stop':
                    log.debug('Added {0} to skip list'.format(chat_sender_id))
                    skip_list.append(chat_sender_id)
                    last_updated = req['update_id']
                    sendMessage(chat_sender_id, "Ok, we won't send you any more messages.")

                if chat_text == '/start':
                    helptext = '''
                        Send `/on` to turn LED on and no surprises for turning it off :p. Also
                        send `/blink` to blink the LED 
                    '''
                    sendMessage(chat_sender_id, helptext)
                    last_updated = req['update_id']

                with open('last_updated.txt', 'w') as f:
                    f.write(str(last_updated))
                    log.debug(
                        'Updated last_updated to {0}'.format(last_updated))
                f.close()
