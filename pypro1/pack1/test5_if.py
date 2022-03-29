# if
var = 5

if var >= 3:
    print('크구나')
    print('참일 때 수행')

print('end1')

print()
if var >= 3:
    #print('크구나2')
    pass
else:
    print('작구나2')

print('end2')

print()
money = 1000
age = 23
if money >= 500:
    item = 'apple'
    if age <= 30:
        msg = 'young'
    else:
        msg = 'old'
else:
    item = 'orange'
    if age > 20:
        msg = 'man'
    else: 
        msg = 'child'
        
print(item, msg)

print()
jum = 99
# jum = int(input('점수 입력')) # input = keyboard로 값 받기
# print(jum, type(jum))
res = ''

if jum >= 90:
    res = 'a'
elif jum >= 70:
    res = 'b'
else:
    res = 'c'
print('res : ' + res)

if 90 <= jum <= 100:
    res = 'a'
elif 70 <= jum < 90:
    res = 'b'
else:
    res = 'c'
print('res : ',res)

print()
names = ['정화', '재이', '일환']
print(names[0])
if '재이' in names:
    print('친구야~')
else:
    print('누구?')
    
    
print()
a = 'kbs'
b = 9 if a == 'kbs' else 11 # 조건을 참조해서 참이면 조건 왼쪽을 아니면 오른쪽을 수행
print(b)    

a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)

print()
a = 3
if a < 5:
    print(0)
elif a < 10:
    print(1)
else:
    print(2)

print(0 if a < 5 else 1 if a<10 else 2)

print()
res = a * 2 if a > 5 else a + 2
print(res)

print((a + 2, a * 2)[a > 5]) #[조건] 참이면 1번째 거짓이면 0번째