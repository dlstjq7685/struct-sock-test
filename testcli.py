#!/usr/bin/env python
"""
client program
"""
from socket import *
import threading
from time import sleep
HOST = 'localhost'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)

class sender(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None,objects=None):
        threading.Thread.__init__(
            self, group=group,
            target=target, name=name)
        self.args = args
        self.kwargs = kwargs
        self.sock = objects
        return

    def run(self):
        while True:
            data = "60frame"
            self.sock.send(bytes(data, 'utf-8'))        
            if data == 'exit':
                break
            sleep(0.017)
        return

class recever(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None,objects=None):
        threading.Thread.__init__(
            self, group=group,
            target=target, name=name)
        self.args = args
        self.kwargs = kwargs
        self.sock = objects
        return

    def run(self):
        while True:
            data = self.sock.recv(BUFSIZE)
            if not data:
                break
            print(data.decode('utf-8'))
        return


def main():
    tcpClisock = socket(AF_INET, SOCK_STREAM)
    tcpClisock.connect(ADDR)
    print('enable connect')

    send_message = sender(objects=tcpClisock)
    rece_message = recever(objects=tcpClisock)
    print('crate thread')

    send_message.start()
    rece_message.start()
    print('started thread')

    send_message.join()
    tcpClisock.close()
    rece_message.join()
    print('end thread')
    
    return 

if __name__=='__main__':
    main()