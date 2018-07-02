from multiprocessing import Process, Pipe
from socket import *

def f(conn):
    temp = []
    while True:
        conn.send(temp)
    conn.close()

def s(conn):
    while True:
        l = conn.recv()
        print(l)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    t = Process(target=s, args=(parent_conn,))
    p.start()
    t.start()

    p.join()
    t.join()
