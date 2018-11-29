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
from time import sleep
import human
import werewolf
import yuyanjia
import nvwu
import lieren


def main():
    fd = foundfd()
    addr = ('127.0.0.1', 8888)
    # fd.sendto('DD你好'.encode(),addr)
    while True:
        b = denglu(fd, addr)
        if b is True:
            break
    q = Queue(maxsize=20)
    p = Process(target=recv_msg, name='Psend', args=(fd, addr, q))
    # p.daemon = True
    p.start()
    while True:
        data = input('输入你要发的消息: ')
        print('可以随意输入消息,1号玩家可以随时开始游戏')
        if q.empty() == False:
            break
        data = 'JA'+data
        fd.sendto(data.encode(), addr)
    recv_msg2(fd, addr)


def recv_msg(fd, addr, q=None):
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
    if data[0:2] == 'OK':
        print('登录成功 , 等待满员开始游戏')
        print('你是%s号玩家'%data[2:])
        return True
    else:
        print(data)
        return False


def foundfd():
    fd = socket(AF_INET, SOCK_DGRAM)
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    return fd


def recv_msg2(fd, addr):
    data = fd.recv(2048)
    print(data.decode())
    if data.decode()[0] == 'L':
        n = data.decode()[1]
        werewolf.Cun(fd, addr, n)
    if data.decode()[0] == 'C':
        n = data.decode()[1]
        human.Cun(fd, addr, n)
    if data.decode()[0] == 'l':
        n = data.decode()[1]
        lieren.Cun(fd,addr,n)
        # pass
    if data.decode()[0] == 'Y':
        n = data.decode()[1]
        yuyanjia.Cun(fd, addr, n)
    if data.decode()[0] == 'N':
        n = data.decode()[1]
        nvwu.Cun(fd, addr, n)
    if data.decode()[0] == 'B':
        pass


if __name__ == "__main__":
    main()
