import threading, time
from threading import Thread, Condition

g_count = 0     # 전역변수는 자동으로 스레드의 공유자원이 됨
lock = Condition()  # thread 공유자원 접근에 제한을 강제하기위한 잠금 객체

def threadCount(id, count):
    global g_count
    
    for i in range(count):
        lock.acquire()      # 공유자원에 대한 충돌 방지
        print('id %s ==> count : %s, g_count : %s'%(id,i,g_count))
        g_count += 1
        lock.release()      # 공유자원에 대한 충돌 방지
        
for i in range(1, 6):
    Thread(target = threadCount, args = (i,5)).start()
    
time.sleep(1)

print('최종 g_count : ', g_count)
print('bye')