

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
        while True:
            data = input('请发言:')
            if data =='OK':
                data = 'A%s'%self.weizhi+'OK'
                return
            else:
                data ='AA'+data
            self.fasong(data, self.addr)
        
    def vote(self):  #vote  投票
        data = input('请投票(15时间决定投票,投票请加DILL数字):')
        if data[0:4] == 'DILL':
            data = data[4:]
            self.data = 'LT'+data
        else:
            self.data = 'LJ'+data
        self.fasong(self.data, self.addr)
        

    def fasong(self, data , addr): #用来发送消息
        self.fd.sendto(data.encode(), addr)

    def dead(self):  #有遗言死
        while True:
            data = input('请输入要说的遗言(输入OK结束发言):')
            if data == 'OK':
                data = 'A%s'%self.weizhi+'OK'
                return
            else:
                data = 'AA'+data
            self.fasong(data, self.addr)
        
    def recv_data(self):
        while True:
            data = self.fd.recv(2048)
            if data.decode()[0] == 'A':
                print(data.decode()[2:])
                if data.decode()[1] == 'L':
                    self.vote()
                elif data.decode()[1] == self.weizhi:
                    print(data.decode()[1])
                    self.say()
            if data.decode()[0] == 'D':
                if data.decode()[1] == self.weizhi:
                    self.dead()
                    break
            elif data.decode()[0:2] == 'LJ':
                print(data.decode()[2:])
            elif data.decode()[1] == 'a':
                print(data.decode()[2:])
                return
        while True:
            data = self.fd.recv(2048)
            if data.decode()[1] == 'a':
                print(data.decode()[2:])
                return
            if data.decode()[0] == 'A':
                print(data.decode()[2:])
            elif data.decode()[0:2] == 'LJ':
                print(data.decode()[2:])

def Cun(fd, addr,n):
    L = Werewolf(fd,n, addr)