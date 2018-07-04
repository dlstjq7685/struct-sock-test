#!/usr/bin/env python
"""
only socket multi server
now error:
    dont close on receive thread
    soulution: multiprocess
"""

from socket import *
import os
import threading
from time import ctime

HOST = 'localhost'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)
LIMIT = 16

#shared object along threads
class shareob(object):

    def __init__(self):
        self.data = None
        self.users = []
        self.isrun = True

#this thread have only one socket client
class submessage(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None,objects=None):
        threading.Thread.__init__(
            self, group=group,
            target=target, name=name)
        self.number = args
        self.kwargs = kwargs
        self.sock = objects
        self.__isrun = True
        return

    def run(self):
        log = open('pid','a')
        log.writelines(str(os.getpid())+ '\n')
        log.close()

        while self.__isrun:
            self.sock.data = self.sock.users[self.number].recv(BUFSIZE)
            if not self.sock.data:
                break
            elif self.sock.data.decode('utf-8') == 'exit':
                self.__isrun = False
                self.sock.users[self.number].close()
                break
        return

#send message all client
class mysendmessage(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None,objects=None):
        threading.Thread.__init__(
            self, group=group,
            target=target, name=name)
        self.args = args
        self.kwargs = kwargs
        self.sock = objects
        self.__isrun = True
        return

    def run(self):
        log = open('pid','a')
        log.writelines(str(os.getpid())+ '\n')
        log.close()

        while self.__isrun:
            if self.sock.data:        
                if self.sock.data == 'out':
                    self.sock.isrun = False

                for idx in range(0, len(self.sock.users)):
                    self.sock.users[idx].send(bytes('[%s] %s' %(ctime(), self.sock.data.decode('utf-8')), 'utf-8'))            
    
                self.sock.data = None
        return

#only listen and fork sub message thread 
class mysocket(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None,objects=None):
        threading.Thread.__init__(
            self, group=group,
            target=target, name=name)
        self.args = args
        self.kwargs = kwargs
        self.objects = objects
        self.__isrun = True
        self.tcpSersock = socket(AF_INET, SOCK_STREAM)
        self.tcpSersock.bind(ADDR)
        self.tcpSersock.listen(LIMIT)

        return

    def run(self):
        submes = []

        while self.__isrun:
            print('waiting for connections')
            tcpCilsock, addr = self.tcpSersock.accept()
            print('connected from ', addr)
            self.objects.users.append(tcpCilsock)
            
            sub = submessage(objects=self.objects, args=len(submes))
            submes.append(sub)
            sub.start()

            if self.objects.data is not None:
                if self.objects.data.decode('utf-8') == 'out':
                    self.__isrun = False
                    for out in submes:
                        out.stop()
                    break

        self.tcpSersock.close()
        return

def main():
    sock = shareob()

    log = open('pid','w')
    log.writelines(str(os.getpid())+ '\n')
    log.close()

    my = mysocket(objects=sock)
    sendme = mysendmessage(objects=sock)
    my.setDaemon(True)
    sendme.setDaemon(True)
    print('start thread')
    my.start()
    sendme.start()
    sendme.join()
    my.join()
    print('end thread')


if __name__=='__main__':
    main()