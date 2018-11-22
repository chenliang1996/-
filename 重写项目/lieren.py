# 村民(CL)
# 属性 : 1.位置()
# 方法 : 1.投票  2.发言  3.死亡
# from fasong import *

class Human:
    '''猎人(lr)
    属性 : 1.位置()
    方法 : 1.投票  2.发言  3.死亡'''
    def __init__(self,fd,addr,weizhi):  #weizhi 人物位置
        self.weizhi = str(weizhi)
        print('你的位置在:'+self.weizhi+'号位置')
        self.fd = fd
        print('你的身份是猎人')
        self.addr = addr
        self.recv_data()
    
    def vote(self):  #vote  投票
        while True:
            data = input('请投票(输入Q弃票):')
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
                data = 'A%s'%self.weizhi+'OK'
                return
            else:
                data = 'A%s'%self.weizhi+data
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
        self.fasong(data, self.addr)


    def dead2(self): #没有遗言死
        pass

    # def jineng(self):  #猎人技能
    #     data = input('请输入要说的射击位置(输入NO取消技能):')
    #     if data == 'NO':
    #         data = 'NO'





    def fasong(self, data , addr): #用来发送消息
        self.fd.sendto(data.encode(),addr)

    def recv_data(self):
        while True:
            data = self.fd.recv(2048)
            # print(data.decode())
            if data.decode()[0] == 'A':
                print(data.decode()[2:])
                if data.decode()[1] == 'T':
                    self.vote()
                elif data.decode()[1] == self.weizhi:
                    print('发言')
                    self.say()
            elif data.decode()[0] == 'D':
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


