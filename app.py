import threading
from flask import Flask, render_template
from lib import bitcoin
from turbo_flask import Turbo
import redis

app = Flask(__name__)
turbo = Turbo(app)
redis = redis.Redis(host='redis', port=6379)

@app.route('/')
def main():
    
    threading.Thread(target=bitcoin.getCurrentPrice,args=(redis, turbo, app)).start()
    threading.Thread(target=bitcoin.getAvgPrice,args=(redis, turbo, app)).start() 
    
    return render_template('index.html')


