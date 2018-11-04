#coding = utf-8
'''
Chatroom
env: python 3.6
socker
'''
from socket import *
import os, sys
from multiprocessing import *
# from 所有的类.human import Human

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


    p = Process(target = recv_msg, name = 'Psend',args=(fd,addr,q))
    p.start()
    while True:
        if q.empty() == False:
            break
        data = input('输入你要发的消息: ')
        data = 'L'+data
        fd.sendto(data.encode(), addr)
    # recv_msg2(fd,addr)

def recv_msg(fd, addr, q = None):
    while True:
        data = fd.recv(2048)
        if data.decode()[0] == 'q':
            q.put(4, block=False)
            print(data.decode()[1:])
        elif data.decode()[0] == 'Q':
            sys.exit(0)
        elif data.decode()[0] =='L':
            print(data.decode()[1:])


if __name__ == '__main__':
    main()
