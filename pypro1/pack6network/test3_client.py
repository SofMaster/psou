# 단순 Client

import socket

clientSock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSock.connect(('192.168.0.10', 7878))
clientSock.sendall('배동현'.encode('UTF-8'))
re_msg = clientSock.recv(1024).decode()
print('수신 자료 : ', re_msg)
clientSock.close()