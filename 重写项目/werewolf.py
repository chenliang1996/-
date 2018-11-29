from multiprocessing import Process

class Werewolf:
    '''角色狼人,可发言,投票,夜晚杀人,自爆直接进入夜晚,死亡'''
    def __init__(self,fd,weizhi,addr):
        self.weizhi = str(weizhi)
        print('你的位置在:'+self.weizhi+'号位置')
        print('你的身份是狼人')
        self.fd = fd
        self.addr = addr
        self.recv_data()
    
    def toupiao(self):
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
            data = input('请发言:')
            if data =='OK':
                data = 'A%s'%self.weizhi+'OK'
                return
            else:
                data ='AA'+data
            self.fasong(data, self.addr)
        
    def vote(self):  #vote  投票
        p = Process(target=recv_from, args=(self.fd,))
        p.start()
        while True:
            data = input('请投票(15秒时间决定投票,投票请加KILL数字):')
            if data[0:4] == 'KILL':
                data = data[4:]
                self.data = 'LT' + data
                break
            else:
                self.data = 'LJ' + data
                self.fasong(self.data, self.addr)
        self.fasong(self.data, self.addr)
        p.join()

    def fasong(self, data , addr): #用来发送消息
        self.fd.sendto(data.encode(), addr)

    def dead(self):  #有遗言死
        while True:
            data = input('请输入要说的遗言(输入OK结束发言):')
            if data == 'OK':
                data = 'A%s' % self.weizhi + 'OK'
                break
            else:
                data = 'AA'+data
            self.fasong(data, self.addr)
        self.fasong(data, self.addr)
        
    def recv_data(self):
        while True:
            data = self.fd.recv(2048)
            data = data.decode()
            if data[0] == 'A' or data[0] =='L':
                print(data[3:])
                if data[1] == 'L':
                    if data[2] == 'T':
                        self.vote()
                elif data[1] == self.weizhi:
                    if data[2] == 'S':
                        self.say()
                elif data[1] == 'A':
                    if data[2] == 'T':
                        self.toupiao()
            if data[0:2] == 'LJ':
                print(data[2:])
            if data[0:3] == 'DDS':
                self.dead()
                break
            if data[0:3] == 'DDW':
                break
            elif data[1] == 'a':
                print(data[2:])
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
    L = Werewolf(fd, n, addr)
    
def recv_from(fd):
    import sys
    while True:
        data = fd.recv(1024)
        data = data.decode()
        if data == 'exit':
            sys.exit(1)
        elif data[0:3] == 'LLJ':
            print(data[3:])

        