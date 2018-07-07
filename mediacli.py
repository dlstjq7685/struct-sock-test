from socket import * 

HOST = 'localhost'
PORT = 8000
ADDR = (HOST, PORT)

if __name__=='__main__':
    csock = socket(AF_INET, SOCK_STREAM)
    csock.connect(ADDR)
    fp  = open('load.png','rb')

    data = "test"
    while True:
        st = fp.readline()
        if not st:
            break
        csock.send(bytes(st))

    fp.close()
    csock.close()
