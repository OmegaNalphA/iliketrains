from flask import Flask
from redis import Redis, RedisError
from twilio.rest import Client
import os
import socket

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Connect to Firebase and set-up database references
cred = credentials.Certificate('./env/iliketrains_firebase_key.json')
firebase_admin.initialize_app(cred, {
   'databaseURL' : 'https://iliketrains-1919.firebaseio.com/'
})
root = db.reference()
train_gate = root.child('train')

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

# Callbacks
def text_user(e):
    destination = root.child('dest')
    if e.data == destination.get():
        # Your Account Sid and Auth Token from twilio.com/console
        account_sid = 'AC0d56f824c7f04685cbf8cc3cf69c00a4'
        auth_token = 'd15d8d6f063d7181f13f792de9d72cb3'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="Here's your stop!",
                            from_='+15127467134',
                            to='+14086406421'
                        )
        # print("[DEBUG] This is where a text to the user would be!")
    else:
        pass
        # print("[DEBUG] Value changed, but doesn't match dest. Doing nothing...")
        
# Flask Stuff
app = Flask(__name__)

def on_server_start():
    # print("[DEBUG] ran on server start")
    train_gate.listen(text_user)

@app.route("/")
def hello():
    print("Hello")
    app.logger.info('testing info log')
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<h4>Inside of route \"/\"</h4>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

@app.route("/hello")
def sendtxt():
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC0d56f824c7f04685cbf8cc3cf69c00a4'
    auth_token = 'd15d8d6f063d7181f13f792de9d72cb3'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Here's your stop!",
                        from_='+15127467134',
                        to='+14086406421'
                    )

    html = "<h3>Hello {name}!</h3>" \
           "<h4>Inside of route \"/hello\"</h4>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    on_server_start()
    app.run(host='0.0.0.0', port=80)