# 村民(CL)
# 属性 : 1.位置()
# 方法 : 1.投票  2.发言  3.死亡
# from fasong import *

class Yyanjia:
    '''预言家(YY)
    属性 : 1.位置()
    方法 : 1.投票  2.发言  3.死亡'''
    def __init__(self,fd,addr,weizhi):  #weizhi 人物位置
        self.weizhi = str(weizhi)
        print('你的位置在:'+self.weizhi+'号位置')
        self.fd = fd
        print('你的身份是预言家')
        self.addr = addr
        self.recv_data()
    
    def vote(self):  #vote  查人
        while True:
            data = input('请投票(要查验的位置):')
            if data not in self.b:
                print('输入有误,重新输入')
                continue
            else:
                self.data = 'YT'+data
                self.fasong(self.data, self.addr)
                break
        

    def toupiao(self):
        while True:
            data = input('请投票(要出局的的位置):')
            if data not in self.b:
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


    def fasong(self, data , addr): #用来发送消息
        self.fd.sendto(data.encode(),addr)

    def recv_data(self):
        import re
        while True:
            data ,addr = self.fd.recvfrom(1024)
            data = data.decode()
            if data[0] == 'A' or data[0] == 'Y':
                print(data[3:])
                if data[1] == 'Y':
                    if data[2] == 'T':
                        self.b = re.findall(r'[1-9]+',data)
                        self.vote()
                elif data[1] == 'A':
                    if data[2] == 'T':
                        self.toupiao()
                elif data[1] == self.weizhi:
                    if data[2] == 'S':
                        self.say()
                    elif data[2] == 'D':
                        self.dead()
                        break
            elif data[3] == 'a':
                print(data[3:])
                return
        while True:
            data = self.fd.recv(2048)
            if data.decode()[0] == 'A':
                print(data.decode()[3:])
            elif data.decode()[3] == 'a':
                print(data.decode()[3:])
                return

    


def Cun(fd, addr,n):
    C = Yyanjia(fd, addr, n)
    
if __name__ == '__main__':
    from socket import *
    fd = socket(AF_INET, SOCK_DGRAM)
    fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    addr = ('127.0.0.1', 8888)
    C = Yyanjia(fd,addr,1)



