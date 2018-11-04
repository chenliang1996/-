#coding = utf-8
'''
Chatroom
env: python 3.6
socker
'''
from socket import *
import os, sys
from select import select
from time import sleep



def main():  #循环接收消息
    fd = socket(AF_INET, SOCK_DGRAM)
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    fd.bind(('0.0.0.0',8888))
    print('等待连接.....端口号8888')
    #执行解析消息函数
    do_request(fd)

def do_request(fd):
    userdist = {}
    userweizhi = {}
    userdist1 = {}
    n = 0
    while True:
        data, addr = fd.recvfrom(1024)
        datalist = data.decode()
        if datalist[0] == 'D':
            n = do_login(fd, addr, datalist[1:], userdist, n, userweizhi, userdist1)
            renman(fd,n,userdist,userdist1,userweizhi)
        if datalist[0] == 'L':
            do_jiaoliu(fd, datalist[1:], addr, userdist,userweizhi,userdist1)


def do_jiaoliu(fd, data, addr, userdist,userweizhi,userdist1):
    name = userdist1[addr]
    data = 'L%s说 %s' % (name, data)
    for i in userweizhi:
        if i != addr:
            fd.sendto(data.encode(),i)



def do_login(fd, addr, username, userdist, n,userweizhi ,userdist1):
    if (username in userdist) or username == '管理员':
        fd.sendto('登录失败,名字已经存在!'.encode(), addr)
        return n
    else:
        n += 1
        fd.sendto('OK'.encode(), addr)
        for i in userdist:
            data = '欢迎%s 来到游戏间 , 还差%d即可开始游戏...'%(username , 8-n)
            fd.sendto(data.encode(), userdist[i])
        userdist[username] = addr
        userweizhi[addr] = n
        # print(userweizhi)
        userdist1[addr] = username
        return n

def renman(fd, n,userdist,userdist1,userweizhi):
    if n == 3:
        for i in userdist:
            data = 'd游戏将在10秒后开始'.encode()
            fd.sendto(data, userdist[i])
        a = 10
        for i in range(10):
            data = 'q%d秒后开始!' % (a)
            for i in userdist:
                fd.sendto(data.encode(), userdist[i])
            sleep(1)
            a -= 1
        for i in userdist:
            fd.sendto('d游戏开始'.encode(),userdist[i])   
        for i in userdist:   #需要关闭子进程 ， 因为子进程无法使用input
                fd.sendto(b'Q', userdist[i])
        begin(fd,userdist,userdist1,userweizhi)

def begin(fd,userdist,userdist1,userweizhi):    #游戏开始后执行函数
    shenfendist = distribute(userweizhi)

def distribute(userweizhi):           #游戏开始的第一步，分发身份信息
    pass

        

    

    
    
    
if __name__ == '__main__':
    main()

        

        



