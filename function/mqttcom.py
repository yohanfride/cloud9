import sys, json, time
import paho.mqtt.client as mqttClient #Must Install Req
mqttConnect = False
broker_address= "localhost"
port = 1883                         
# user = "yourUser"
# password = "yourPassword"
client = mqttClient.Client("Python")  

def publish(topic,message):
    client.connect(broker_address, port=port)
    time.sleep(0.5)
    client.publish(topic,json.dumps(message))
    client.disconnect()
    return

 

