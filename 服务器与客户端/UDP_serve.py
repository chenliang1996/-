#coding = utf-8
'''
Chatroom
env: python 3.6
socker
'''
from socket import *
import os
import sys
from select import select
from time import sleep
#前缀W代表全员消息 , 不做处理
# Q 退出子进程
# q 游戏开始
# T 投票
# S 说话
# *1相同身份的人


def main():  # 循环接收消息
    fd = socket(AF_INET, SOCK_DGRAM)
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    fd.bind(('0.0.0.0', 8888))
    print('等待连接.....端口号8888')
    # 执行解析消息函数
    do_request(fd)


def do_request(fd):
    userdist = {}
    userweizhi = {}
    userdist1 = {}
    n = 0
    L1 = []
    while True:
        try:
            data, addr = fd.recvfrom(1024)
            datalist = data.decode()
            if datalist[0] == 'D':
                n = do_login(fd, addr, datalist[1:],
                            userdist, n, userweizhi, userdist1)
                renman(fd, n, userdist, userdist1, userweizhi)
            if datalist[1] == 'J':
                do_jiaoliu(fd, datalist[2:], addr, userdist, userweizhi, userdist1)
            if datalist[0] == 'L':
                pass
            if datalist[1] == 'W':
                fasong(fd,datalist[2:],userdist)
            if datalist[1] == 'T':
                toupiao(L1, datalist, userweizhi)
        except ConnectionResetError:
            main()



def toupiao(L, data, userweizhi):
    if datalist[0] == 'L':  # 狼人投票刀人
        pass
    elif datalist[0] == 'Y':  # 预言家投票验人
        pass
    elif datalist[0] == 'l':  # 猎人投票带走人
        pass
    elif datalist[0] == 'N':  # 女巫投票毒人
        pass
    elif datalist[0] == 'n':  # 女巫投票救人
        pass
    elif datalist[0] == 'A':  # 白天投票出局人
        L.append(int(datalist[2:]))
        chulitoup(L, userweizhi)


def chulitoup(L, userweizhi):
    max_count = 0
    max_list = []
    for i in L:
        if L.count(i) > max_count:
            max_str = i
            max_count = L.count(i)
    max_list.append(max_str)
    L.remove(max_str)
    for i in L:
        if L.count(i) == max_count:
            max_list.append(i)
    if len(max_list) == 1:
        dead(fd, max_list[0])


def do_jiaoliu(fd, data, addr, userdist, userweizhi, userdist1):
    name = userdist1[addr]
    data = 'W%s说 %s' % (name, data)
    for i in userdist1:
        if i != addr:
            fd.sendto(data.encode(), i)


def do_login(fd, addr, username, userdist, n, userweizhi, userdist1):
    if (username in userdist) or username == '管理员':
        fd.sendto('登录失败,名字已经存在!'.encode(), addr)
        return n
    else:
        n += 1
        fd.sendto('OK'.encode(), addr)
        for i in userdist:
            data = '欢迎%s 来到游戏间 , 还差%d即可开始游戏...' % (username, 8-n)
            fd.sendto(data.encode(), userdist[i])
        userdist[username] = addr
        userweizhi[addr] = n
        # print(userweizhi)
        userdist1[addr] = username
        return n


def renman(fd, n, userdist, userdist1, userweizhi):
    if n == 3:
        for i in userdist:
            data = 'W游戏将在10秒后开始'.encode()
            fd.sendto(data, userdist[i])
        a = 10
        for i in range(10):
            data = 'q%d秒后开始!' % (a)
            for i in userdist:
                fd.sendto(data.encode(), userdist[i])
            sleep(1)
            a -= 1
        for i in userdist:
            fd.sendto('W游戏开始'.encode(), userdist[i])
        for i in userdist:  # 需要关闭子进程 ， 因为子进程无法使用input
            fd.sendto(b'Q', userdist[i])
        begin(fd, userdist, userdist1, userweizhi)


def begin(fd, userdist, userdist1, userweizhi):  # 游戏开始后执行函数
    shenfendist = distribute(userweizhi)
    sendStatus(fd, shenfendist, userweizhi)
    sleep(3)
    # 执行游戏循环流程
    liucheng(fd, shenfendist,userdist1)


def liucheng(fd, shenfendist,userdist1):  # 天黑了
    day = 0
    while True:
        if panduan(shenfendist) == 'WIN':
            data = 'Aa游戏结束,狼人失败'
            fasong(fd,data,userdist1)
            main()
            break
        elif panduan(shenfendist) == 'FAIL':
            data = 'Aa游戏结束,狼人胜利'
            fasong(fd,data,userdist1)
            main()
            break
        day += 1
        data = 'AA-----第%d天----' % day
        fasong(fd,data,userdist1)
        data = 'AY--预言家请睁眼验人--'
        fasong(fd,data,userdist1)
        data = 'AL--狼人请睁眼,决定杀人对象--'
        fasong(fd,data,userdist1)
        data = 'AN--女巫请睁眼,决定救人还是毒人--'
        fasong(fd,data,userdist1)
        tianliang(fd, userdist1, 0, shenfendist)
        toupiao(fd,shenfendist)


def tianliang(fd,userdist1,n,shenfendist):  # 天亮了
    data = 'AA--天亮了,昨晚%d号玩家死亡--' % n
    fasong(fd, data, userdist1)
    dead(fd,n,shenfendist)
    data = 'A%d--从%d玩家开始发言' % (n+1, n+1)
    fasong(fd,data,userdist1)


def distribute(userweizhi):  # 游戏开始的第一步，分发身份信息
    from random import shuffle
    if len(userweizhi) == 3:
        # L = ['L', 'L', 'L', 'C', 'C', 'Y', 'N', 'l']
        L = ['C','C','L']
        shuffle(L)  # 把列表顺序打乱
        shenfendist = dict(zip(userweizhi, L))
        return shenfendist
    if len(userweizhi) > 8 and len(userweizhi) < 16:
        pass


def sendStatus(fd, shenfendist, userweizhi):  # 发送身份信息 , 等待3秒开始游戏流程
    for a, b in shenfendist.items():
        data = b+str(userweizhi[a])
        fd.sendto(data.encode(), a)
    for a in shenfendist:
        fd.sendto('AW确认身份,3秒开始游戏'.encode(), a)

def toupiao(fd, shenfendist):
    data = 'AT请开始投票'
    fasong(fd,data,shenfendist)

def fasong(fd,data,userlist):
    for i in userlist:
        fd.sendto(data.encode(), i)


def dead(fd, n, shenfendist):
    data = 'D' + str(n)
    for i in shenfendist:
        fd.sendto(data.encode(), i)
    del shenfendist[i]


def panduan(shenfendist):
    if 'L' not in list(shenfendist.values()):
        return 'WIN'
    elif 'C' not in list(shenfendist.values()) and 'Y' not in list(shenfendist.values()) and 'N' not in list(shenfendist.values()) and 'l' not in list(shenfendist.values()):
        return 'FAIL'
    else:
        return


if __name__ == '__main__':
    main()
