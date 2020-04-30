from tornado.web import Application, RequestHandler, ErrorHandler
from tornado.ioloop import IOLoop
from function.db import dbmongo
from routes import init as route_init
from bson import ObjectId
import traceback
import json 

db = dbmongo()

def make_app(): 
  urls = route_init.list_url
  # print()
  # sys.stdout.flush()
  return Application(urls, debug=False)
  
if __name__ == '__main__':
  app = make_app()
  app.listen(3001)
  IOLoop.instance().start()