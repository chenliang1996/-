from socket import *
import os
import sys
import select
from time import sleep
from multiprocessing import *

fd = socket(AF_INET, SOCK_DGRAM)
fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
addr = ('127.0.0.1', 8888)


def shouxiaoxi(fd):
    while True:
        data = fd.recv(1024)
        print(data.decode(),2)


def fun(fd):
    fd.sendto(b'ok', addr)
    while True:
        data = fd.recv(1024)
        print(data.decode(),1)

if __name__ == '__main__':
    p = Process(target=shouxiaoxi, args=(fd,))
    p.start()
    fun(fd)