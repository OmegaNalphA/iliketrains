from gpiozero import DistanceSensor
import time
import math

gate_1_sensor = DistanceSensor(echo=4, trigger=22)
gate_2_sensor = DistanceSensor(echo=16, trigger=21)
#ultrasonic.threshold_distance = 0.2

active_gate = 'none'

while True:
    if gate_1_sensor.distance > 0:
        gate_1_status = True
        active_gate = 'gate_1'
    else:
        gate_1_status = False
    print('gate 1 distance: ' + str(gate_1_sensor.distance))
    
    if gate_2_sensor.distance > 0:
        gate_2_status = True
        active_gate = 'gate_2'
    else:
        gate_2_status = False
    print('gate 2 distance: ' + str(gate_2_sensor.distance))
    
    if gate_1_status is False and gate_2_status is False:
        active_gate = 'none'
    print('active gate is : ' + active_gate)

    
    time.sleep(0.2)