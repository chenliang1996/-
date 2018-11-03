from socket import *
fd = socket(AF_INET,SOCK_DGRAM)
fd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
addr = ('127.0.0.1',12345)
# fd.bind(('127.0.0.1',12345))

def fasong(data , addr):
    fd.sendto(data.encode(),addr)



