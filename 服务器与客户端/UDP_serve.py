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
    global userdist
    global userweizhi
    global userdist1
    global n
    # global L1
    userdist = {}
    userweizhi = {}
    userdist1 = {}
    n = 0
    # L1 = []
    while True:
        fd.setblocking(False)
        fd.settimeout(20)
        try:
            data, addr = fd.recvfrom(1024)
            datalist = data.decode()
        except:
            datalist = '  '
        # print(n)
        finally:
            if datalist[0] == 'D':
                if n == 3:
                    datalist = 'gfs' + datalist
                    fd.sendto('Q人已经满了'.encode(),addr)
                else:
                    n = do_login(fd, addr, datalist[1:],
                                userdist, n, userweizhi, userdist1)
            elif datalist[1] == 'J':
                do_jiaoliu(fd, datalist[2:], addr, userdist, userweizhi, userdist1)
            elif datalist[0] == '1':
                if datalist[1] == 'K':
                    break
            if n == 3:
                fasong(fd,'W人已经满了,1号玩家可以输入K开始游戏',userweizhi)
    begin(fd,userdist,userdist1,userweizhi)

def begin(fd,userdist, userdist1, userweizhi):  # 游戏开始后执行函数
    for i in userdist:
        data = 'W游戏将在5秒后开始'.encode()
        fd.sendto(data, userdist[i])
    a = 5
    for i in range(5):
        data = 'W%d秒后开始!' % (a)
        for i in userdist:
            fd.sendto(data.encode(), userdist[i])
        sleep(1)
        a -= 1
    for i in userdist:
        fd.sendto('q游戏开始,输入OK进入游戏'.encode(), userdist[i])
    for i in userdist:  # 需要关闭子进程 ， 因为子进程无法使用input
        fd.sendto(b'Q', userdist[i])
    shenfendist = distribute(userweizhi)
    sendStatus(fd, shenfendist, userweizhi)
    sleep(3)
    # 执行游戏循环流程
    day = 0
    while True:
        day = liucheng(fd, shenfendist, userdist1,day)
        data = 'AA请死者说遗言'
        fasong(fd,data,userdist1)
        n = 1
        b = int(DD[0])+1
        DD.clear()
        while True:
            fayan(fd,userweizhi,userdist1)
            n += 1
            if n == len(userweizhi):
                break
            data = 'A%d--请%d玩家发言' % (b,b)
            fasong(fd,data,userdist1)
            b += 1

def fayan(fd,userweizhi,userdist1):
    while True:
        fd.settimeout(10)  #等待10秒
        try:
            data,addr = fd.recvfrom(1024)
            data = data.decode()
        except:
            data = 'AA发言时间到'
            fasong(fd, data, userweizhi)
            return
        else:
            if data[2:]=='OK':
                data = 'AA%s号玩家发言结束' %data[1]
                for i in userweizhi:
                    if i != addr:
                        fd.sendto(data.encode(), i)
                break
            elif data[0] == 'A':
                data = 'AA%s号玩家说 %s' % (data[1],data[2:])
                for i in userweizhi:
                    if i != addr:
                        fd.sendto(data.encode(), i)
    
    
def liucheng(fd, shenfendist,userdist1,day):  # 天黑了
    L = []  #狼人,白天投票列表
    l = []  #预言家等投票列表
    global DD
    DD = []  #死亡列表
    AF = panduan(shenfendist)
    print(AF)
    if AF == 'WIN':
        data = 'Aa游戏结束,狼人胜利'
        fasong(fd,data,userdist1)
        main()
    elif AF == 'FAIL':
        data = 'Aa游戏结束,狼人失败'
        fasong(fd,data,userdist1)
        main()
    day += 1
    data = 'AA-----第%d天----' % day
    fasong(fd, data, userdist1)
    data = 'AY--预言家请睁眼验人--'
    fasong(fd, data, userdist1)
    S = toupiao(fd, l, DD)
    if not S:
        S =''
    chulitoupY(fd,shenfendist,userweizhi,S)
    data = 'AL--狼人请睁眼,决定杀人对象--'
    fasong(fd, data, userdist1)
    L = toupiao(fd, L,DD)
    DD.append(chulitoupL(fd,L,shenfendist))
    data = 'AN--女巫请睁眼,决定救人还是毒人--'
    fasong(fd, data, userdist1)
    s = L[0]
    if not s:
        data = 'NN--昨晚没有死人'
    else:
        data = 'NN--昨晚死的是%s'%s
    fasong(fd,data,userdist1)
    S = toupiao(fd,l,DD)
    tianliang(fd, userdist1, DD, shenfendist)
    # toupiao(fd, shenfendist,DD)
    return day


def toupiao(fd, L, DD):
    while True:
        try:
            fd.setblocking(False)
            fd.settimeout(15)
            data, addr = fd.recvfrom(1024)
            datalist = data.decode()
            # print(datalist)
        except:
            return L
        else:
            if datalist[0] == 'L':  # 狼人投票刀人
                if datalist[1] == 'J':
                    do_jiaoliu(fd,datalist,addr,userdist,userweizhi,userdist1)
                    continue
                elif datalist[1]=='T':
                    L.append(datalist[2:])
            elif datalist[0] == 'Y':  # 预言家投票验人
                return datalist[2:]
            elif datalist[0] == 'l':  # 猎人投票带走人
                return datalist[2:]
            elif datalist[0] == 'N':  # 女巫投票毒人
                DD.append(datalist[2:0])
                return
            elif datalist[0] == 'n':  # 女巫投票救人
                DD.remove(datalist[2:])
                return 
            elif datalist[0] == 'A':  # 白天投票出局人
                if datalist[2:] is not '':
                    L.append(datalist[2:])
            return L

def chulitoupY(fd,shenfendist,userweizhi,S):
    if not S:
        data = 'YY没有验人'
    else:
        for i in userweizhi:
            if userweizhi[i] == S:
                data = shenfendist[i]
                break
        data = 'YY %s玩家的身份为%s' % (S, data)
    fasong(fd,data,shenfendist)
    


def chulitoupL(fd,L,shenfendist):  #狼人投票处理
    max_count = 0
    if len(L) == 1:
        return L[0]
    else:
        for i in L:
            if L.count(i) > max_count:
                max_str = i
                max_count = L.count(i)
    return max_str

        
def chulitoupB(fd, L, userweizhi):  #白天投票处理
    max_count = 0
    max_list = []
    if len(L) == 1:
        dead(fd,L,shenfendist)
    else:
        for i in L:
            if L.count(i) > max_count:
                max_str = i
                max_count = L.count(i)
        max_list.append(max_str)
        L.remove(max_str)
        for i in L:
            if L.count(i) == max_count:
                max_list.append(i)
        if len(max_list) > 1:
            for i in max_list:
                for k in userweizhi:
                    if i == userweizhi[k]:
                        data = 'A%s%s玩家上PK台,请在次发言'%(i,i)
                        fd.sendto('A%s%s玩家和%s玩家上PK台,请在次发言'.encode(),k)
    


def do_jiaoliu(fd, data, addr, userdist, userweizhi, userdist1):
    if data[0:2] == 'LJ':
        name = userweizhi[addr]
        data = 'LJ%s说%s' % (name, data[2:])
    else:
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
            data = 'W欢迎%s 来到游戏间 , 还差%d即可开始游戏...' % (username, 8-n)
            # print(data)
            fd.sendto(data.encode(), userdist[i])
        userdist[username] = addr
        userweizhi[addr] = str(n)
        # print(userweizhi)
        userdist1[addr] = username
        return n


def tianliang(fd, userdist1, DD, shenfendist):  # 天亮了
    if len(DD) == 1:
        data = 'AA--天亮了,昨晚%s号玩家死亡--' % DD[0]
    elif len(DD) == 0:
        data = 'AA--昨晚平安夜--'
    elif len(DD) > 1:
        data = 'AA--天亮了,昨晚%s号和%s玩家死亡--' % (DD[0],DD[1])
    fasong(fd, data, userdist1)
    dead(fd,DD,shenfendist)

    


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

def fasong(fd,data,userlist):
    for i in userlist:
        fd.sendto(data.encode(), i)


def dead(fd, DD, shenfendist):
    for i in DD:
        data = 'D' + i
        for a in shenfendist:
            fd.sendto(data.encode(), a)
        for b, c in userweizhi.items():
            if c == i:
                del shenfendist[b]
                print(shenfendist)
                del userweizhi[b]
                print(userweizhi)
                break

def panduan(shenfendist):
    L = list(shenfendist.values())
    print(L)
    print(L.count('L'))
    print(len(L) / 2)
    if L.count('L') >= len(L) / 2:
        return 'WIN'
    elif 'L' not in L:
        return 'FAIL'


if __name__ == '__main__':
    main()
