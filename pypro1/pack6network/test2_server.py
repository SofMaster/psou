# 단순 Echo Server

from socket import *

serverSock = socket(AF_INET,SOCK_STREAM)   #socket(소켓종류, 소켓유형)
serverSock.bind(('127.0.0.1', 8888))    # server 열기
serverSock.listen(1)     #tcp listener 설정
print('Server Start')

conn, addr = serverSock.accept()    # 연결 대기 blocking, client 연결 대기하는 역할, 무한 loop 상태
print('Client addr : ', addr)
print('from client message : ', conn.recv(1024).decode())   #client로부터 메시지를 받아 디코딩
conn.close()
serverSock.close()  # server 끝내기
