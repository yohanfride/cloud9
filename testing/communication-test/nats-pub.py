from pynats import NATSClient
import argparse
import json
from datetime import datetime

broker = "161.117.58.227"#"127.0.0.1"
port = "4222"
subject = 'message/sensor/j7k67b' #'message/sensor/py787b'

client = NATSClient("nats://"+broker+":"+port,socket_timeout=2, verbose=True)
client.connect()
today = datetime.today() #current-datetime
msg = {
    "device_code":"j7k67b-wa51", #"py787b-mw47",
    "date_add":round(datetime.today().timestamp() * 1000), #today.strftime("%Y-%m-%d %H:%M:%S"),
    "gps":{
        "latitude":-7.575973,
        "longitude":112.878304
    },
    "temperature": 25.5,
    "fuel":1000
}
payload = json.dumps(msg)
client.publish(subject, payload=payload)
client.close()