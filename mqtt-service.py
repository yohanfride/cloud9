import sys, json, time
import paho.mqtt.client as mqttClient #Must Install Req
from function import *
from controller import comChannelController

topic_list = {} 
Connected = False
broker_address= "localhost"
port = 1883                         
# user = "yourUser"
# password = "yourPassword"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                
        Connected = True   
        subscribe_list()             
    else:
        print("Connection failed")
 
def on_message(client, userdata, message):
    raw_msg = message.payload.decode("utf-8")
    try:
        raw_object = json.loads(raw_msg)
    except:
        raw_object = {"failed":True}
    if message.topic == 'mqtt/service/subscribe' :
        on_message_subscribe(raw_object)
    elif message.topic == 'mqtt/service/unsubscribe' :
        on_message_unsubscribe(raw_object)
    else :
        print("-------New Message-----------")
        print(message.topic);                 
        print(raw_object);                 
        print("-----------------------------")
    
    
def on_message_subscribe(message):
    topic = message['topic']
    channel_code = message['channel_code']
    topic_list[topic] = channel_code
    client.subscribe(topic)
    print("Subscribe Topic: "+topic)

def on_message_unsubscribe(message):
    topic = message['topic']
    channel_code = message['channel_code']
    topic_list[topic] = channel_code
    client.unsubscribe(topic)
    print("Unsubscribe Topic: "+topic)
    try:
        del topic_list[topic]
    except KeyError:
        pass

def subscribe_list():
    query = {
        "active":True,
        "channel_type": "mqtt"
    }
    result = comChannelController.find(query)
    for val in result['data']:
        topic_list[val['topic']] = val['channel_code']
        client.subscribe(val['topic'])
        print("Subscribe Topic: "+val['topic'])
 
client = mqttClient.Client("Python3")               
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      
client.on_message= on_message                      
client.connect(broker_address, port=port)          
client.loop_start()        
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
client.subscribe("mqtt/service/subscribe")
client.subscribe("mqtt/service/unsubscribe")

try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()