from socket import *
import os
import sys
from select import select
from time import sleep

fd = socket(AF_INET, SOCK_DGRAM)
fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
fd.bind(('0.0.0.0', 8888))
print('等待连接.....端口号8888')


data, addr = fd.recvfrom(1024)
print(data)
while True:
    fd.sendto(b'OK', addr)
    sleep(5)
    print('发送OK')

if __name__ == '__main__':
    pass
