import threading
from flask import Flask, render_template, request
import requests
from turbo_flask import Turbo
import time
import redis
import os
app = Flask(__name__)
turbo = Turbo(app)
redis = redis.Redis(host='redis', port=6379)
print(str(os.system('ls')))
def getCurrentPrice():
    global redis
    while True:
        # request's response
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        # get the http request's response as a json object
        data = response.json()
        redis.set('current_price', data["bpi"]["USD"]["rate"]) 
        with app.app_context():
            turbo.push(turbo.replace(render_template('current_price.html',CurrentPrice=redis.get('current_price')),  'CurrentPrice'))
        time.sleep(1)
        
def getAvgPrice():
    global redis
    sum = 0
    while True:
        # request's response
        response = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10')
        # get the http request's response as a json object
        data = response.json()
        for i in range(10):
            # sum the prices in approximately in one minute
            sum = sum + (data['Data']["Data"][i]['close'])
        # average in last 10 minutes
        redis.set('avg_price', sum / 10)  
        with app.app_context():
            turbo.push(turbo.replace(render_template('avg_price.html',AvgPrice=redis.get('avg_price')),  'AvgPrice'))
        time.sleep(3)
        
@app.route('/')
def BitcoinPrice():
    
    threading.Thread(target=getCurrentPrice).start()
    threading.Thread(target=getAvgPrice).start() 
    return render_template('index.html')
