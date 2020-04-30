#!/usr/bin/python3

import sys
from bson import ObjectId
import json 
from function import *



sensors = []
db = db.dbmongo()

collection = "sensor"

def add(fillData):    
    result = db.insertData(collection,fillData)
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
    result = db.findOne(collection,query,None)
    if result == []:
        response = {"status":False, "data":data}               
    else:
        response = {"status":True, 'message':'Success','data':result}
    return cloud9Lib.jsonObject(response)

def update(query,data):    
    if data == []:
        return {"status":False, "message":"UPDATE NONE"}    
    result = db.updateData(collection,query,data)
    if result == []:
        response = {"status":False, "message":"UPDATE FAILED"}               
    else:
        response = {'status':True,'message':'Success','data':result}
    return cloud9Lib.jsonObject(response)

def delete(id):        
    query = {"_id":ObjectId(id)}
    result = db.deleteData(collection,query)
    if result == []:
        response = {"status":False, "message":"DELETE FAILED"}               
    else:
        response = {'status':True,'message':'Success','data':result}
    return cloud9Lib.jsonObject(response)