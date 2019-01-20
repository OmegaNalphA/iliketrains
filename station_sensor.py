from gpiozero import DistanceSensor
import time
import math

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

print("Establishing connection to Firebase...")
cred = credentials.Certificate('iliketrains_account_key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://iliketrains-1919.firebaseio.com/'
    })
print("Connecting to Firebase! Getting root node...")

root = db.reference()
train_gate = root.child('train')
print("Initial train station value: " + train_gate.get())


gate_2_sensor = DistanceSensor(echo=4, trigger=22)
gate_1_sensor = DistanceSensor(echo=16, trigger=21)
#gate_1_sensor.threshold_distance = 0.4
#gate_2_sensor.threshold_distance = 0.4

active_gate = 'none'

while True:
    if gate_1_sensor.distance > 0:
        active_gate = 'gate_1'
        train_gate.set("1")
        print('gate 1 distance: ' + str(gate_1_sensor.distance))
    
    elif gate_2_sensor.distance > 0:
        active_gate = 'gate_2'
        train_gate.set("2")
        print('gate 2 distance: ' + str(gate_2_sensor.distance))
    
    else:
        active_gate = 'none'
        #train_gate.set("null")
    print('active gate is : ' + active_gate)

    time.sleep(0.8)
