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
    global minzidict
    minzidict = {'Y':'好人','C':'好人','L':'狼人','l':'好人','N':'好人'}
    n = 0
    while True:
        data, addr = fd.recvfrom(1024)
        # 第一步为登录(DD)
        data = data.decode()
        print(data)
        if data[0:2] == 'DD':
            b = chulidenglu(fd, data, addr, weizhidict, mingzidict, n)
            if n == 4:
                fd.sendto('人数已满'.encode(), addr)
                continue
            if b is False:
                continue
            else:
                weizhidict = b[0]
                mingzidict = b[1]
                n = b[2]
            print('当前人数是', n, '个')
        print(weizhidict, mingzidict, n)
        if data[0] == 'J':  # 所有的交流都用这个判断处理,所有消息都发送给所有人,所有人都会接受,不同的前缀处理显示问题
            jiaoliu(fd, addr, data, weizhidict)
        if data[2:] == 'Begin':
            if weizhidict[addr] == '1':
                break
    begin(fd, weizhidict)
    shenfendict, shenfenlist = secv_shenfen(fd, weizhidict)
    weizhilist = list(weizhidict.values())
    # 第一步,判断游戏是否需要继续进行;若狼人数量超过总人数的一半即以上则游戏结束
    # 狼人获胜,反之继续.若狼人全部死亡,则狼人失败.
    day = 0
    #shenfendict 是 addr为键,身份为值
    Ydict = dict(zip(weizhidict.values(), shenfenlist))  #死亡的人这里也要删除
    Ldict = Ydict.copy()
    print(Ydict)
    while True:
        # if panduan(shenfenlist) == None:
        day += 1
        data = 'AAW-----第%d天----' % day
        fasong(fd, data, weizhidict)
        data = 'AAW--预言家请睁眼验人--'
        fasong(fd, data, weizhidict)
        s = ','.join(list(Ydict))
        data = 'AYT--未查验的人有%s号玩家--' %s
        fasong(fd, data, weizhidict)
        # data = 'A1S1号玩家发言'
        # fasong(fd, data, weizhidict)
        Ychuli(fd, Ydict)
        data = 'AAW--狼人请投票刀人--'
        fasong(fd, data, weizhidict)
        S = ','.join(list(Ldict))
        data = 'ALT--现在存活的玩家有%s号玩家--' %S
        fasong(fd, data, weizhidict)
        ab = []
        ab = Lchuli(fd, Ldict, weizhidict,ab)
        print(ab)
        k = Lchuli2(fd, Ldict, ab)
        data = 'LLW--你们杀死的玩家是%s--'%k
        fasong(fd, data, weizhidict)
        



def Lchuli2(fd, Ldict, L):#狼人投票处理
    max_count = 0
    if len(L) == 1:
        return L[0]
    else:
        for i in L:
            if L.count(i) > max_count:
                max_str = i
                max_count = L.count(i)
    print(max_str,'狼人杀人对象')
    return max_str

def Lchuli(fd, Ldict,weizhidict,ab):# 狼人投票第一步处理,收集所有狼人的投票情况
    n = list(Ldict.values()).count('L')
    while True:
        try:
            data, addr = fd.recvfrom(1024)
            data = data.decode()
        except:
            n -= 1
            if n == 0:
                break
            continue
        if data[0:2] == 'LJ':
            data1 = 'LLJ%s号玩家说%s' % (weizhidict[addr], data[2:])
            fasong(fd, data, weizhidict)
        elif data[0:2]=='LT':
            ab.append(data[2:])
            n -= 1
            if n == 0:
                break
            print(n,'狼人个数')
    return ab


def Ychuli(fd, Ydict,):
    try:
        fd.setblocking(False)
        fd.settimeout(15)
        data, addr = fd.recvfrom(1024)
        data = data.decode()
    except:
        return Ydict
    else:
        data1 = 'YYW%s号玩家的身份是%s' % (data[2:], minzidict[Ydict[data[2:]]])
        fasong(fd, data1, weizhidict)
        del Ydict[data[2:]]
        



def panduan(L):
    print(L.count('L'))
    print(len(L) / 2)
    if L.count('L') >= len(L) / 2:
        return 1
    elif 'L' not in L:
        return 2


def fasong(fd, data, userlist):  # 发送函数,发送给指定字典或列表中的人.
    for i in userlist:
        fd.sendto(data.encode(), i)


def secv_shenfen(fd, weizhidict):  # 一共10个if
    from random import shuffle
    if len(weizhidict) == 3:
        # L = ['L', 'C', 'Y', 'N']
        L = ['Y','L','L']
        shuffle(L)  # 把列表顺序打乱
    elif len(weizhidict) == 6:
        L = ['L', 'C', 'Y', 'N']
        shuffle(L)  # 把列表顺序打乱
    elif len(weizhidict) == 7:
        L = ['L', 'C', 'Y', 'N']
        shuffle(L)  # 把列表顺序打乱
    elif len(weizhidict) == 8:
        L = ['L', 'C', 'Y', 'N']
        shuffle(L)  # 把列表顺序打乱
    elif len(weizhidict) == 9:
        L = ['L', 'C', 'Y', 'N']
        shuffle(L)  # 把列表顺序打乱
    shenfendist = dict(zip(weizhidict, L))
    for i in shenfendist:
        data = shenfendist[i]+str(weizhidict[i])
        fd.sendto(data.encode(), i)
    return shenfendist, L


def begin(fd, weizhidict):  # 游戏开始后执行函数(目的关闭客户端的子进程)
    for i in weizhidict:
        data = 'W游戏将在5秒后开始'.encode()
        fd.sendto(data, i)
    for i in range(5, 1, -1):
        data = 'JA%d秒后开始!' % (i)
        for i in weizhidict:
            fd.sendto(data.encode(), i)
        sleep(1)
    for i in weizhidict:
        fd.sendto('q游戏开始,输入OK进入游戏'.encode(), i)
    for i in weizhidict:  # 需要关闭子进程 ， 因为子进程无法使用input
        fd.sendto(b'Q', i)


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
            data = '欢迎%s进入房间,还差%d的人满员' % (data[2:], (4-int(n)))
            fd.sendto(data.encode(), i)
        n += 1
        weizhidict[addr] = str(n)
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
    pass


if __name__ == "__main__":
    main()
