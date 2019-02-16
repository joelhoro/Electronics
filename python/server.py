
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import json

config = [
    {
        'name': 'Upper arm',
        'channel': 0,
        'position': 100,
    },
    {
        'name': 'Body',
        'channel': 1,
        'position': 65,
    },
    {
        'name': 'Gripper',
        'channel': 2,
        'position': 0,
    },
    {
        'name': 'Lower arm',
        'channel': 3,
        'position': 70,
    },
]




class MainHandler(tornado.web.RequestHandler):
  def get(self):
    loader = tornado.template.Loader(".")
    self.write(loader.load("index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
  def send(self, message, data):
    self.write_message({'name': message, 'data': data})
  def open(self):
    print('connection opened...')
    self.send('config',config)

  def on_message(self, message):
    try:
        obj = json.loads(message)
        name = obj['name']
        if 'data' in obj:
          data = obj['data']
        else:
          data = None
        print('received %s => %s' % (name, data))
    except:
        print("Could not parse message %s" % message)
        
  def on_close(self):
    print( 'connection closed...')

application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "."}),
])

if __name__ == "__main__":
  port = 9090
  application.listen(port)
  print("Listening on %s" % port)
  tornado.ioloop.IOLoop.current().start()
