#coding = utf-8
'''
Chatroom
env: python 3.6
socker
'''
from socket import *
import os
import sys
from multiprocessing import *

def main():
    fd = foundfd()
    addr = ('176.215.133.165', 8888)
    # fd.sendto('DD你好'.encode(),addr)
    while True:
        b = denglu(fd, addr)
        if b is True:
            break
    q = Queue(maxsize=20)
    p = Process(target=recv_msg, name='Psend', args=(fd, addr, q))
    # p.daemon = True
    p.start()
    while True:0
        if q.empty() == False:
            break
        data = input('输入你要发的消息: ')
        data = 'JA'+data
        fd.sendto(data.encode(), addr)
    input('结束:')

def recv_msg(fd, addr, q = None):
    while True:
        data = fd.recv(2048)
        if data.decode()[0] == 'q':
            q.put(4, block=False)
            print()
            print(data.decode()[1:])
        elif data.decode()[0] == 'Q':
            sys.exit(0)
        elif data.decode()[0:2] == 'JA':
            print()
            print(data.decode()[2:])


def denglu(fd, addr):
    name = input('请输入登录名: ')
    data = 'DD'+name
    fd.sendto(data.encode(), addr)
    # data1 = fd.recvfrom(1024)
    data = fd.recv(1024)
    data = data.decode()
    if data == 'OK':
        print('登录成功 , 等待满员开始游戏')
        return True
    else:
        print(data)
        return False


def foundfd():
    fd = socket(AF_INET, SOCK_DGRAM)
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    return fd


if __name__ == "__main__":
    main()
