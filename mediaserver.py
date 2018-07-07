from socket import *

HOST = 'localhost'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)
LIMIT = 16

if __name__=='__main__':
    msock = socket(AF_INET, SOCK_STREAM)
    msock.bind(ADDR)
    msock.listen(LIMIT)
    fpp = open('test.png', 'wb')

    mcli, addr = msock.accept()

    while True:
        message = mcli.recv(BUFSIZE)
        st = message
        if not st:
            break
        fpp.write(st)

    fpp.close()
    msock.close()