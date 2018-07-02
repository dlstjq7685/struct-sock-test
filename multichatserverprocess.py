from multiprocessing import Process, Pipe
from socket import *


HOST = 'localhost'
PORT = 12345
BUFSIZE = 1024
ADDR = (HOST, PORT)
LIMIT = 16

#shared object along threads
class shareob(object):

    def __init__(self):
        self.data = None
        self.users = []
        self.isrun = True


def listener(conn, objects=None):
    tcpSersock = socket(AF_INET, SOCK_STREAM)
    tcpSersock.bind(ADDR)
    tcpSersock.listen(LIMIT)
    subpro = []

    while True:
        print('waiting for connections')
        tcpCilsock, addr = tcpSersock.accept()
        print('connected from ', addr)
        
        sub = Process(target=sub_reader, args=tcpCilsock)
        subpro.append(sub)
        sub.start()
        temp = tcpCilsock
        conn.send(temp)
        conn.close()

def allsender(child, objects=None):

    socklist = []

    while True:
        temp = child.recv()

        if temp is not None:
            socklist.append(temp)




def sub_reader(objects=None):
    print('test')

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    
    superprocess = Process(target=listener, args=parent_conn)
    senderprocess = Process(target=allsender, args=child_conn)
    #sprocess = Process(target=sub_reader, args=parent_conn)

    superprocess.start()
    senderprocess.start()

    senderprocess.join()
    superprocess.join()
