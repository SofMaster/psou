# 문1) 2 ~ 9 단 모두 출력
print()
for dan in range(2,10):
    print('--{}단--'.format(dan))
    for n in range(1,10):
        print('{0}*{1}={2}'.format(dan,n,n*dan))
        
        
# 문2) 1 ~ 100 사이의 정수 중 3의 배수이면서 5의 배수의 합 출력
print()
i = list(range(1,101))
hap = 0
for a in i:
    if a % 3 == 0 and a % 5 == 0:
        hap += a 
        
print('1~100 사이 3의 배수이면서 4의 배수인 숫자의 합계: ', hap)


# 문3) 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# 예) 1 3
# 예) 2 2
print()
for a in range(1,7):
    for b in range(1,7):
        if(a + b)%4 == 0:
            print('a + b = 4의 배수인 경우: ' + str(a) + "" + str(b))