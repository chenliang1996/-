# global A
from socket import *
fd = socket(AF_INET, SOCK_DGRAM)
fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
addr = ('127.0.0.1', 8888)

fd.setblocking(False)
fd.settimeout(5)
try :
    data = fd.recv(1024)
    print(data)
    fd.settimeout(3)
    data = fd.recv(1024)
    print(data)
except:
    print('时间到了')
fd.setblocking(True)
# fd.sendto(b'gfd',('127.0.0.1',8888))
data, addr = fd.recvfrom(1024)
print(data)




# def ds():
#     global A
#     A = [1]
#     print('A为全局')

# def sd():
#     # global A
#     A.append(2)
#     jk()

# def jk():
#     print(A)

# def gjk():
#     print(A)

# ds()
# sd()
# gjk()