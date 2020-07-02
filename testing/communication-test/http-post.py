import requests
from datetime import datetime
import json

token = "jjn7jpy787b26u8ux"
url = "http://localhost:3001/comdata/sensor/"+token+"/"
today = datetime.today()
msg = {
    "device_code":"py787b-qo06",
    "date_add":today.strftime("%Y-%m-%d %H:%M:%S"),
    "gps":{
        "latitude":-7.475973,
        "longitude":112.978304
    },
    "temperature": 25.5,
    "fuel":1000
}
payload = json.dumps(msg)
headers = {
    'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data = payload)
print(response.text.encode('utf8'))
    
