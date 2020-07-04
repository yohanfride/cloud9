#!/usr/bin/python3
import paho.mqtt.client as paho
import json,time
from datetime import datetime
t = round(datetime.today().timestamp() * 1000)
print(t)
# time.sleep(5)
# s = round(datetime.today().timestamp() * 1000)
# print(s)
# print(s - t)
# print(isinstance(today,int))

try:
    today = datetime.utcfromtimestamp(round(t))
except:
    today = datetime.utcfromtimestamp(round(t/1000))

print(today.strftime("%Y-%m-%d %H:%M:%S"))
