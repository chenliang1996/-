# 村民(CL)
# 属性 : 1.位置()
# 方法 : 1.投票  2.发言  3.死亡
# from fasong import *

class Nvwu:
    '''女巫(NW)
    属性 : 1.位置()
    方法 : 1.投票  2.发言  3.死亡'''
    def __init__(self,fd,addr,weizhi):  #weizhi 人物位置
        self.weizhi = str(weizhi)
        print('你的位置在:'+self.weizhi+'号位置')
        self.fd = fd
        print('你的身份是女巫')
        self.addr = addr
        self.recv_data()
    
    def vote(self):  #vote  投票
        while True:
            data = input('请投票(救人请输入Q+位置,毒人输入D+位置):')
            if data[1:] not in self.b:
                print('输入有误,重新输入')
                continue
            elif data[0] == 'D':
                data = data[1:]
                self.data = 'nT'+data
            elif data[0] == 'Q':
                self.data = 'NT' + data
            self.fasong(self.data, self.addr)
            break
        

    def toupiao(self):
        while True:
            data = input('请投票要出局的位置(输入Q弃票):')
            if data == 'Q':
                data = 'AT'
                self.fasong(self.data, self.addr)
                break
            try:
                int(data)
            except:
                print('输入有误,重新输入')
                continue
            else:
                self.data = 'AT'+data
                self.fasong(self.data, self.addr)
                break


    def say(self):
        while True:
            data = input('请输入要说的言论(输入OK结束输入):')
            if data == 'OK':
                data = 'A%s' % self.weizhi + 'OK'
                break
            else:
                data = 'A%s'%self.weizhi+data
            self.fasong(data, self.addr)
        self.fasong(data,self.addr)

    def dead(self):  #有遗言死
        while True:
            data = input('请输入要说的遗言(输入OK结束输入):')
            if data == 'OK':
                data = 'A%s' % self.weizhi + 'OK'
                break
            else:
                data = 'A%s' % self.weizhi + data
            self.fasong(data,self.addr)   
        self.fasong(data,self.addr)


    def dead2(self): #没有遗言死
        pass

    def fasong(self, data , addr): #用来发送消息
        self.fd.sendto(data.encode(),addr)

    def recv_data(self):
        import re
        while True:
            data = self.fd.recv(2048)
            data = data.decode()
            # print(data.decode())
            if data[0] == 'A' or data[0]=='N':
                print(data[3:])
                if data[1] == 'A':
                    if data[2] == 'T':
                        self.toupiao()
                elif data[1] == self.weizhi:
                    if data[2] == 'S':
                        self.say()
                    elif data[2] == 'D':
                        self.dead()
                        break
                elif data[1] == 'N':
                    self.b = re.findall(r'[1-9]+',data)
                    self.vote()
            elif data[1] == 'a':
                print(data[3:])
                return
        while True:
            data = self.fd.recv(2048)
            if data.decode()[0] == 'A':
                print(data.decode()[3:])
            elif data.decode()[1] == 'a':
                print(data.decode()[3:])
                return

    


def Cun(fd, addr,n):
    C = Nvwu(fd, addr, n)
    
if __name__ == '__main__':
    A = Nvwu(1,456,3)
    # A.vote()
    A.say()
    A.dead()


