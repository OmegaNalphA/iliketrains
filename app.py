from flask import Flask
from redis import Redis, RedisError
from twilio.rest import Client
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
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
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+14086406421',
                        to='+14086406421'
                    )

    print(message.sid)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)