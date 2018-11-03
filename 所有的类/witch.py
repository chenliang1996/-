from human import *
from fasong import *
class Witch(Human):

    def poison(self):   #毒药
        poi = input("请输入要毒的位置")
        poi = "P "+poi
        fasong(poi,self.addr)

    def antidote(self):   #解药
        ant = input("请是不是要救他!")
        ant = "A "+ant
        fasong(ant,self.addr)       

if __name__ =="__main__":
    B = Witch(1262,('127.0.0.1',12345))
    B.poison()
    B.antidote()