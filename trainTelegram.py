import random
import os
import requests
import logging
import json
import geocoder
import time
import pandas as pd
import math
import csvkit
import subprocess

def store_data(source,dest):
    subprocess.check_output('csvcut -c 1,2,6,7,9,11 isl_wise_train_detail_03082015_v1.csv | csvgrep -c 5 -m {} |csvgrep -c 6 -m {} |csvlook > trainresult.csv'.format(source,dest),shell=True)

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

def message(chat_id,source,dest):
    store_data(source,dest)
    df = pd.read_csv('trainresult.csv')
    for i in range(2,df.shape[0]):
        try:
            result=df.values[i][0].split("|")
            formatted=[i.strip(" ") for i in result]
            trainCode=formatted[1]
            trainName=formatted[2]
            trainArrival=formatted[3]
            trainDept=formatted[4]
            sendMessage(chat_id,'TrainCode : {}, Train Name : {}, Arrival Time : {} ,Departure Time : {}'.format(trainCode,trainName,trainArrival,trainDept) )
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
                g=chat_text.split(" to ")
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
                       Send STN1 to STN2. STN1 == Station Code Source ; STN2 == Station Code for Destination 
                    '''
                    sendMessage(chat_sender_id, helptext)
                    last_updated = req['update_id']

                with open('last_updated.txt', 'w') as f:
                    f.write(str(last_updated))
                    log.debug(
                        'Updated last_updated to {0}'.format(last_updated))
                f.close()

