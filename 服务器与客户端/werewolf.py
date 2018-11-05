

class Werewolf:
    '''角色狼人,可发言,投票,夜晚杀人,自爆直接进入夜晚,死亡'''
    def __init__(self,fd,weizhi,addr):
        self.weizhi = str(weizhi)
        print(self.weizhi)
        print('你的身份是狼人')
        self.fd = fd
        self.addr = addr
        self.recv_data()
    
    def toupiao(self):
        data = input('请投票(请输入数字,q弃票):')
        return data


    def say(self):
        data = input('请发言:')
        data ='AA'+data
        self.fasong(data, self.addr)
        
    def vote(self):  #vote  投票
        data = input('请投票(回车弃票):')
        self.data = 'CT'+data
        self.fasong(self.data, self.addr)
        

    def fasong(self, data , addr): #用来发送消息
        self.fd.sendto(data.encode(), addr)

    def dead(self):  #有遗言死
        data = input('请输入要说的遗言:')
        data = 'AA'+data
        self.fasong(data, self.addr)
        
    def recv_data(self):
        while True:
            data = self.fd.recv(2048)
            if data.decode()[0] == 'A':
                print(data.decode()[2:])
                if data.decode()[1] == 'T':
                    self.vote()
                elif data.decode()[1] == self.weizhi:
                    print(data.decode()[1])
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
    L = Werewolf(fd,n, addr)