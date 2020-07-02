import requests
from datetime import datetime
import json
import time
import sys
import random

token = "jjn7jpy787b26u8ux"
url = "http://localhost:3001/comdata/sensor/"+token+"/"
for x in range(1000):
    today = datetime.today()
    msg = {
        "device_code":"py787b-qo06",
        "date_add":today.strftime("%Y-%m-%d %H:%M:%S"),
        "gps":{
            "latitude":-7.475973 + (random.randint(1,1000) / 10000 ),
            "longitude":112.978304 - ( random.randint(1,1000) / 10000 )
        },
        "temperature": random.randint(2000,3500) / 100,
        "fuel":950
    }
    payload = json.dumps(msg)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
    sys.stdout.flush()
    time.sleep(5)
