#coding = utf-8
'''
Chatroom
env: python 3.6
socker
'''
from socket import *
import os, sys
from multiprocessing import *
import human
import werewolf
import yuyanjia
import nvwu

def main():
    fd = socket(AF_INET, SOCK_DGRAM)
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    addr = ('127.0.0.1', 8888)
    q = Queue(maxsize=20)
    while True:
        name = input('请输入登录名: ')
        data = 'D'+name
        fd.sendto(data.encode(),addr)
        # data1 = fd.recvfrom(1024)
        data1 = fd.recv(1024)
        datalist = data1.decode().split(' ')
        if datalist[0] == 'OK':
            print('登录成功 , 等待满员开始游戏')
            break
        else:
            print(data1.decode())
    p = Process(target=recv_msg, name='Psend', args=(fd, addr, q))
    # p.daemon = True
    p.start()
    while True:
        if q.empty() == False:
            break
        data = input('输入你要发的消息: ')
        if data == 'exit':
            return
        elif data == 'K':
            data = '1K'
        elif data == 'OK':
            continue
        else:
            data = 'AJ'+data
        fd.sendto(data.encode(), addr)
    recv_msg2(fd,addr)

def recv_msg(fd, addr, q = None):
    while True:
        data = fd.recv(2048)
        if data.decode()[0] == 'q':
            q.put(4, block=False)
            print()
            print(data.decode()[1:])
        elif data.decode()[0] == 'Q':
            sys.exit(0)
        elif data.decode()[0] == 'W':
            print()
            print(data.decode()[1:])

def recv_msg2(fd, addr):
    data = fd.recv(2048)
    if data.decode()[0] == 'L':
        n = int(data.decode()[1])
        werewolf.Cun(fd,addr,n)
    if data.decode()[0] == 'C':
        n = int(data.decode()[1])
        human.Cun(fd,addr,n)
    if data.decode()[0] == 'l':
        # n = int(data.decode()[1])
        # lieren.Cun(fd,addr,n)
        pass
    if data.decode()[0] == 'Y':
        n = int(data.decode()[1])
        yuyanjia.Cun(fd,addr,n)
    if data.decode()[0] == 'N':
        n = int(data.decode()[1])
        nvwu.Cun(fd,addr,n)
    if data.decode()[0] == 'B':
        pass






if __name__ == '__main__':
    main()
