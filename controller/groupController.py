#!/usr/bin/python3

import sys
from bson import ObjectId
import json 
from function import *



sensors = []
db = db.dbmongo()

collection = "group"

def add(fillData):  
    insertQuery = {
        'company_id':fillData.get('company_id', None),
        'name':fillData.get('name', None),
        'add_by':fillData.get('add_by', None),
        'active':True 
    }
    result = db.insertData(collection,insertQuery)
    if result == []:
        response = {'status':False, 'message':"Add Failed"}               
    else:
        response = {'status':True,'message':'Success','data':result}
    return cloud9Lib.jsonObject(response)

def find(query):  
    result = db.find(collection,query)
    if result == []:
        response = {"status":False, "data":data}               
    else:
        response = {'status':True, 'data':result}    
    return cloud9Lib.jsonObject(response)

def findOne(query):  
    result = db.findOne(collection,query, None)
    if result is None:
        response = {"status":False, "data":query}               
    else:
        response = {'status':True,'message':'Success','data':result}    
    return cloud9Lib.jsonObject(response)

def update(query,data):            
    updateData = {}
    if 'company_id' in data: updateData['company_id'] = data['company_id']
    if 'name' in data: updateData['name'] = data['name']
    if 'active' in data: updateData['active'] = data['active']

    if updateData == []:
        return {"status":False, "message":"UPDATE NONE"}        
    result = db.updateData(collection,query,updateData)
    if not result :
        response = {"status":False, "message":"UPDATE FAILED"}               
    else:
        response = {'status':True,'message':'Success','data':result}
    return cloud9Lib.jsonObject(response)

def delete(query):            
    result = db.deleteData(collection,query)
    if not result:
        response = {"status":False, "message":"DELETE FAILED"}               
    else:
        response = {'status':True,'message':'Success','data':result}
    print("**********RESPONSE*************")
    print (response)
    print("**********RESPONSE*************")
    sys.stdout.flush()
    return cloud9Lib.jsonObject(response)