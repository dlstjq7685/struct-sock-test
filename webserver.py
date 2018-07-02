from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from datetime import datetime
import sys
#pip install git+http://github.com/dpallot/simple-websocket-server.git
class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        self.sendMessage(self.data)

    def handleConnected(self):
        print(datetime.now())
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('localhost', 8000, SimpleEcho)
server.serveforever()
