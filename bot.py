from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import pandas as pd
from pandas.io.json import json_normalize 
import numpy as np

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'covid' in incoming_msg:
        # return a quote
        r = requests.get("https://www.trackcorona.live/api/countries")
        if r.status_code == 200:
            a = r.json()['data']
            df = json_normalize(a) 
            df.sort_values(by ='confirmed', axis=0, ascending=False, inplace=True, kind='quicksort', na_position='last')
            df.reset_index(drop=True,inplace=True)
            confirmed=df['confirmed'].sum()
            dead=df['dead'].sum()
            recovered=df['recovered'].sum()
            quote = 'Confirmed :- {}\n Deadth :- {}\n Recovered :- {}'.format(confirmed,dead,recovered)
        
            msg.body(quote)

        else:
            quote = 'I could not retrieve information at this time, sorry !'
        responded = True
    if not responded:
        msg.body('I only know covid information, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()