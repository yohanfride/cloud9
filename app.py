from tornado.web import Application, RequestHandler, ErrorHandler
from tornado.ioloop import IOLoop
from function.db import dbmongo
from routes import init as route_init
from bson import ObjectId
import traceback
import json 
import sys
import asyncio

db = dbmongo()
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
def make_app(): 
  urls = route_init.list_url
  return Application(urls, debug=False)
  
if __name__ == '__main__':
  app = make_app()
  app.listen(3001)
  IOLoop.instance().start()