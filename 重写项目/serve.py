#coding = utf-8
'''
Chatroom
env: python 3.6
socker
'''
from socket import *
import os
import sys
from time import sleep


def main():  # 循环接收消息 并针对处理
    fd = foundfd()
    # 建立人员储存字典1(addr为键,n(位置)为值)
    global weizhidict
    weizhidict = {}
    # 建立人员姓名字典2(addr为键,名字为值)
    global mingzidict
    mingzidict = {}
    n = 0
    while True:
        data, addr = fd.recvfrom(1024)
        # 第一步为登录(DD)
        data = data.decode()
        print(data)
        if data[0:2] == 'DD':
            print(n)
            if n == 3:
                fd.sendto('人数已满'.encode(), addr)
                continue
            b = chulidenglu(fd, data, addr, weizhidict, mingzidict, n)
            if b is False:
                continue
            else:
                weizhidict = b[0]
                mingzidict = b[1]
                n = b[2]
        print(weizhidict, mingzidict, n)
        if data[0] == 'J':  # 所有的交流都用这个判断处理,所有消息都发送给所有人,所有人都会接受,不同的前缀处理显示问题
            jiaoliu(fd, addr, data, weizhidict)
        if data[2:] == 'Begin':
            if weizhidict[addr] == 1:
                break
    begin(fd, weizhidict,n)

def begin(fd,weizhidict,n):  # 游戏开始后执行函数
    for i in weizhidict:
        data = 'W游戏将在5秒后开始'.encode()
        fd.sendto(data, i)
    for i in range(5,1,-1):
        data = 'JA%d秒后开始!' % (i)
        for i in weizhidict:
            fd.sendto(data.encode(), i)
        sleep(1)
    for i in weizhidict:
        fd.sendto('q游戏开始,输入OK进入游戏'.encode(), i)
    for i in weizhidict:  # 需要关闭子进程 ， 因为子进程无法使用input
        fd.sendto(b'Q', i)
    # shenfendist = distribute(userweizhi,n)
    # sendStatus(fd, shenfendist, userweizhi)
    # sleep(3)
    # # 执行游戏循环流程
    # day = 0
    # while True:
    #     day = liucheng(fd, shenfendist, userdist1,day)
    #     data = 'AA请死者说遗言'
    #     fasong(fd,data,userdist1)
    #     n = 1
    #     b = int(DD[0])+1
    #     DD.clear()
    #     while True:
    #         fayan(fd,userweizhi,userdist1)
    #         n += 1
    #         if n == len(userweizhi):
    #             break
    #         data = 'A%d--请%d玩家发言' % (b,b)
    #         fasong(fd,data,userdist1)
    #         b += 1


def foundfd():  # 创建fd
    fd = socket(AF_INET, SOCK_DGRAM)
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    fd.bind(('0.0.0.0', 8888))
    print('等待连接.....端口号8888')
    return fd


def chulidenglu(fd, data, addr, weizhidict, mingzidict, n):  # 处理登录函数
    if addr in weizhidict:
        fd.sendto('登录失败'.encode(), addr)
        return False
    elif data[2:] in mingzidict.values():
        fd.sendto('名字已经存在'.encode(), addr)
        return False
    else:
        fd.sendto(b'OK', addr)
        for i in weizhidict:
            fd.sendto(('欢迎%s进入房间' % data[2:]).encode(), i)
        n += 1
        weizhidict[addr] = n
        mingzidict[addr] = data[2:]
        return weizhidict, mingzidict, n


def jiaoliu(fd, addr, data, weizhidict):
    if data[2:] == 'exit':
        '''此if用来后期做开始游戏前退出'''
        fd.sendto('Q'.encode(), addr)
    else:
        n = weizhidict[addr]
        data = '%s%s号玩家说%s' % (data[0:2], n, data[2:])
        print(data)
        for i in weizhidict:
            if i != addr:
                fd.sendto(data.encode(), i)


def liucheng():
    

if __name__ == "__main__":
    main()
