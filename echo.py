from socket import *

HOST = '0.0.0.0'
PORT = 8000
BUFSIZE = 1024
ADDR = (HOST, PORT)
LIMIT = 16

if __name__=='__main__':
    msock = socket(AF_INET, SOCK_STREAM)
    msock.bind(ADDR)
    msock.listen(LIMIT)

    mcli, addr = msock.accept()
    print(addr, "connected")
    message = mcli.recv(BUFSIZE)
    print(message.decode())
    msock.close()