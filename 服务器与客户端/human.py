# 村民(CL)
# 属性 : 1.位置()
# 方法 : 1.投票  2.发言  3.死亡
# from fasong import *

class Human:
    '''村民(CL)
    属性 : 1.位置()
    方法 : 1.投票  2.发言  3.死亡'''
    def __init__(self,fd,addr,weizhi):  #weizhi 人物位置
        self.weizhi = str(weizhi)
        print(self.weizhi)
        self.fd = fd
        print('你的身份是村民')
        self.addr = addr
        self.recv_data()
    
    def vote(self):  #vote  投票
        data = input('请投票(回车弃票):')
        self.data = 'CT'+data
        self.fasong(self.data,self.addr)

    def say(self):
        data = input('请发言:')
        data ='AA'+data
        self.fasong(data,self.addr)

    def dead(self):  #有遗言死
        data = input('请输入要说的遗言:')
        data = 'AA'+data
        self.fasong(data,self.addr)


    def dead2(self): #没有遗言死
        pass

    def fasong(self, data , addr): #用来发送消息
        self.fd.sendto(data.encode(),addr)

    def recv_data(self):
        while True:
            data = self.fd.recv(2048)
            print(data.decode())
            if data.decode()[0] == 'A':
                print(data.decode()[2:])
                if data.decode()[1] == 'T':
                    self.vote()
                elif data.decode()[1] == self.weizhi:
                    print('发言')
                    self.say()
            if data.decode()[0] == 'd':
                if data.decode()[1] == self.weizhi:
                    self.dead()
                    break
            elif data.decode()[1] == 'a':
                print(data.decode()[2:])
                return
        while True:
            data = self.fd.recv(2048)
            if data.decode()[0] == 'A':
                print(data.decode()[2:])
            elif data.decode()[1] == 'a':
                print(data.decode()[2:])
                return

    


def Cun(fd, addr,n):
    C = Human(fd, addr, n)
    
if __name__ == '__main__':
    A = Human(1,456)
    # A.vote()
    A.say()
    A.dead()


