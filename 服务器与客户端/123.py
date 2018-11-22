from socket import *


fd = socket(AF_INET, SOCK_DGRAM)
fd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
fd.bind(('0.0.0.0', 8888))
print('等待连接.....端口号8888')
data, addr = fd.recvfrom(1024)

fd.sendto(b'Y',addr)


