from datetime import datetime
from flask import Flask
import random
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return"<p>Hello, World!</p>"


@app.route('/goodbye/')
def goodbye_world():
    return "<p>Goodbye, World!</p>"

@app.route("/coder/")
def coder():
    return "<p>This  web app was created in a class at Coder Academy.</p>"

@app.route('/current_time/')
def current_time():
    now = datetime.now()
    time = now.strftime('%H:%M')
    return  f'<p>{time}</p>'

@app.route('/coinflip')
def coinflip():
    coin = ['heads', 'tails']
    result = random.choice(coin)
    
    conflip_dict = {
        'result': result
    }
    return json.dumps(conflip_dict)