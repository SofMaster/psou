# Echo Server : 서비스를 계속 유지
import socket
import sys

HOST = '192.168.0.8'
PORT = 7878

serSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serSock.bind((HOST, PORT))
    serSock.listen(5) # 동시 최대 접속 수 : 1 ~ 5 한번에 들어올 수 있는 접속
    print('서버 서비스 중 ...')
    while True:
        conn, addr = serSock.accept()
        print('client info : ', addr[0], addr[1])
        print(conn.recv(1024).decode())     #메시지 수신
        
        # 메시지 송신
        conn.send(('from server : ' + str(addr[0]) + ', 너도 잘 지내라~').encode('UTF_8'))
    
    
except Exception as e:
    print('err : ', e)
    sys.exit()
finally:
    serSock.close()
    conn.close()