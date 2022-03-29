# 반복문 : while 조건
from sqlalchemy.sql.expression import false
a = 1

while a <= 5:
    print(a, end = ' ') #end = ' ' 커서를 한칸 이동
    a = a + 1
    
print('\nwhile 종료')

print()
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i:' + str(i) + ', j:' + str(j))
        j += 1
    i += 1
    
print('\nwhile 종료2')

print('1 ~ 100 사이의 정수 중 3의 배수의 합')
i = 1; hap = 0
while i <= 100:
    #print(i, end = ' ')
    if i % 3 == 0:
        #print(i, end = ' ')
        hap += i
    i += 1
    
print('합은', hap)   

print()
colors = ['r', 'g', 'b']
print(len(colors))
a = 0
while a < len(colors):
    print(colors[a], end = ':')
    a += 1 
    
print()
while colors:
    print(colors.pop())
    
print(len(colors))

print() ##
i = 1
while i <= 10:
    j = 1
    res = ''
    while j <= i:
        res = res + '*'
        j += 1
    print(res)
    i += 1
    
    
    
# 문1) 1 ~ 100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
i = 1
hap = 0
while i<=100:
    while i % 3 == 0:
        while i % 2 == 1:
            print('3의 배수이나 2의 배수가 아닌 수 : ',i)
            hap += i
            print('합은 : ',hap)
            i += 1
        i += 1 
    i += 1     

# 문2) 2 ~ 5 까지의 구구단 출력
print()
x = 2
while x <= 5:
    y=1
    while y<10: 
        #print(i+'단 : '+'i'+' * '+'j'+'=',i*j)
        print(x,'x',a,'=',x*a, end = '')
        y += 1
    print()
    x+=1 


# 문3) -1, 3, -5, 7, -9, 11 ~ 99 까지의 합을 출력
print()
i = -1
hap = 0
while 1:
    hap += i
    if i<0:
        i=i*(-1)+2
    else:
        i = i*(-1)-2
    if i == -101:
        break
    
print('합은', hap)

#문4) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
aa = 2; count = 0
while aa <= 100:
    imsi = False
    bb = 2
    while bb <= aa -1:
        if aa % bb == 0:
            imsi = True
        bb += 1
        
    if imsi == False:
        print(aa,end = '')
        count += 1
        
    aa += 1
    
print('갯수 : ', count)

