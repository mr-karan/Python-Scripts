import random
import os
import requests
import logging
import json
import geocoder
import time
import pandas as pd
import math
df = pd.read_csv('HospitalDirectory.csv')
def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
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

BOT_KEY = ''
API_BASE = 'https://api.telegram.org/bot'

def get_updates():
    log.debug('Checking for requests')
    return json.loads(requests.get(API_BASE + BOT_KEY + '/getUpdates', params = {'offset': last_updated + 1}).text)


def sendMessage(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(API_BASE + BOT_KEY + '/sendMessage', data = payload)

def message(chat_id,lat,lng):
    for i in range(df.shape[0]):
        try:
            if(distance((float(df.values[i][21]),float(df.values[i][22])),(lat,lng))<=5.0):
                sendMessage(chat_id,"Name : {} , Address :{} , Phone :{} ".format(df.values[i][1],df.values[i][5],df.values[i][10]))
                last_updated = req['update_id']

        except:
            pass


if __name__ == '__main__':
    log.debug('Starting up')
    log.debug('Last updated id: {0}'.format(last_updated))
    while (True):
        r = get_updates()
        if r['ok']:
            for req in r['result']:
                chat_sender_id = req['message']['chat']['id']
                chat_text = req['message']['text']
                g = geocoder.google(chat_text).latlng
                if len(g)==0:
                    print('Must be a typo, please check')
                message(chat_sender_id,g[0],g[1])
                last_updated = req['update_id']
                log.debug('Chat text received: {0}'.format(chat_text))    	
                if chat_text == '/stop':
                    log.debug('Added {0} to skip list'.format(chat_sender_id))
                    skip_list.append(chat_sender_id)
                    last_updated = req['update_id']
                    sendMessage(chat_sender_id, "Ok, we won't send you any more messages.")

                if chat_text == '/start':
                    helptext = '''
                       Send me your location to get a list of all hospitals near your area within 5km radius. 
                    '''
                    sendMessage(chat_sender_id, helptext)
                    last_updated = req['update_id']

                with open('last_updated.txt', 'w') as f:
                    f.write(str(last_updated))
                    log.debug(
                        'Updated last_updated to {0}'.format(last_updated))
                f.close()

