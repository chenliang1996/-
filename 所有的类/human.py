# 村民(CL)
# 属性 : 1.位置()
# 方法 : 1.投票  2.发言  3.死亡
from fasong import *

class Human:
    '''村民(CL)
    属性 : 1.位置()
    方法 : 1.投票  2.发言  3.死亡'''
    def __init__(self,weizhi,addr):  #weizhi 人物位置
        self.weizhi = weizhi
        self.addr = addr
    
    def vote(self):  #vote  投票
        data = input('请投票(回车弃票):')
        self.data = 'V '+data
        fasong(self.data,self.addr)

    def say(self):
        data = input('请发言:')
        fasong(data,self.addr)

    def dead(self):  #有遗言死
        data = input('请输入要说的遗言:')
        self.data = 'D '+data
        fasong(self.data,self.addr)


    def dead2(self): #没有遗言死
        pass


if __name__ == '__main__':
    A = Human(1,456)
    # A.vote()
    A.say()
    A.dead()


