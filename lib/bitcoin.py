import requests
from flask import Flask, render_template
import time


def getCurrentPrice(redis, turbo, app):
    while True:
        # get the http request's response as a json object and save it to redis database
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        redis.set('current_price', data["bpi"]["USD"]["rate"]) 
        # update the GUI
        with app.app_context():
            turbo.push(turbo.replace(render_template('current_price.html',CurrentPrice=str(redis.get('current_price').decode('UTF-8'))),  'CurrentPrice'))
        time.sleep(3)
        
        
        
def getAvgPrice(redis, turbo, app):
    sum = 0
    while True:
        # get the http request's response as a json object and save it to redis database
        response = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10')
        data = response.json()
        for i in range(10):
            # sum the prices in one minute
            sum = sum + (data['Data']["Data"][i]['close'])
        redis.set('avg_price', sum / 10)  
        
        # update the GUI
        with app.app_context():
            turbo.push(turbo.replace(render_template('avg_price.html',AvgPrice=str(redis.get('avg_price').decode('UTF-8'))),  'AvgPrice'))
        time.sleep(3)
        
