"""
use this server
"""
from socket import *
from time import sleep, ctime
from multiprocessing import Process, Manager, Value

HOST = 'localhost'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)
LIMIT = 16

#all client send
def sender(clist,flag,data):
    while flag.value:
        if len(data) > 0 :
            if data[0] :
                for i in range(0,len(clist)):
                    clist[i].send(bytes('[%s] %s' %(ctime(), data[0]), 'utf-8'))
                data.pop()

#one client one receiver
def receiver(sock,flag, data):
    temp = None    
    while flag.value:
        temp = sock.recv(BUFSIZE)
        data.append(temp.decode('utf-8'))
        print(data)

#only clientsocket listen
def listener(clist,flag,data):
    tcpSersock = socket(AF_INET, SOCK_STREAM)
    tcpSersock.bind(ADDR)
    tcpSersock.listen(LIMIT)

    p = []
    idx = 0
    while flag:
        print('waiting for connections')
        tcpCilsock, addr = tcpSersock.accept()
        print('connected from ', addr)

        clist.append(tcpCilsock)
        p.append(Process(target=receiver, args=(tcpCilsock, flag, data)))
        p[idx].start()
        idx += 1

if __name__=="__main__":
    man = Manager()
    dman = Manager()
    clist = man.list()
    data = dman.list()
    flag = Value('i', True)

    lis = Process(target=listener, args=(clist,flag,data))
    sen = Process(target=sender, args=(clist,flag,data))

    lis.start()
    sen.start()

    lis.join()
    sen.join()