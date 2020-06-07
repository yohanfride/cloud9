#!/usr/bin/python3
from pynats import NATSClient
import argparse
import json
import sys, json, time

broker_address = "127.0.0.1"
port = "4222"
client = NATSClient("nats://"+broker_address+":"+port,verbose=True)

def publish(topic,message):
    print(topic)
    print(message)
    sys.stdout.flush()
    client.connect()
    client.publish(topic, payload=json.dumps(message))
    client.close()
    return