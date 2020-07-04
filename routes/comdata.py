import sys
sys.path.append('../')
from tornado.web import RequestHandler
from bson import ObjectId
import json 
from function import *
from controller import comChannelController
from controller import commETLController
from controller import commLogController
import datetime 
from pytz import timezone

groups = []
db = db.dbmongo()

#PRIMARY VARIABLE - DONT DELETE
define_url = [
    ['sensor/([^/]+)/','add']
]

class add(RequestHandler):
  def post(self,token_access):    
    data = json.loads(self.request.body)
    if not token_access:
        response = {"status":False, "message":"Token Acces not found",'data':json.loads(self.request.body)}               
        self.write(response)
        return
    #Log Insert#
    remote_ip = self.request.headers.get("X-Real-IP") or \
            self.request.headers.get("X-Forwarded-For") or \
            self.request.remote_ip
    insertLog = {
        'token_access' : token_access,
        'ip_sender':remote_ip,
        'channel_type':'http-post',
        'raw_message':data
    }
    #End Log Insert#
    queryGroup = {
        'token_access' : token_access,
        'active': True 
    }
    resultChannel = comChannelController.findOne(queryGroup)
    if not resultChannel['status']:
        response = {"status":False, "message":"Token Access not match",'data':json.loads(self.request.body)} 
        insertLog['response'] = response
        commLogController.add(insertLog);
        self.write(response)
        return              
    else:
        channelData = resultChannel['data']

    infoHttp = {
        'token_access' : token_access,
        'ip_sender':remote_ip,
        'channel_type':'http-post',
    }
    if 'date_add' in data :
        try:
            if(isinstance(message['date_add'],int)):
                infoMqtt['date_add_sensor_unix'] = message['date_add']
                try:
                    today = datetime.fromtimestamp(round(message['date_add']),timezone('Asia/Jakarta')) #datetime.fromtimestamp(round(message['date_add']))
                except:
                    today = datetime.fromtimestamp(round(message['date_add']/1000),timezone('Asia/Jakarta')) #datetime.fromtimestamp(round(message['date_add']/1000))
                infoMqtt['date_add_sensor'] = today
            else:
                infoMqtt['date_add_sensor'] = datetime.strptime(message['date_add'],'%Y-%m-%d %H:%M:%S')
        except:
            infoHttp['date_add_sensor'] = data['date_add']
    else :
        infoHttp['date_add_sensor'] = None

    if 'device_code' in data :
        insert = commETLController.etl(channelData['collection_name'],infoHttp,data['device_code'],data)
    else :
        insert = commETLController.nonetl(channelData['collection_name'],infoHttp,data)
    
    if not insert['status']:
        response = {"status":False, "message":"Failed to add", 'data':json.loads(self.request.body)}               
    else:
        response = {'message':'Success','status':True}    
    insertLog['response'] = response
    commLogController.add(insertLog);
    self.write(response)