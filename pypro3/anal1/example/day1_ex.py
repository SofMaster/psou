# step1 : array 관련 문제
# 정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 각 행 단위로 합계, 최댓값을 구하시오.
import numpy as np
aa = np.array(np.random.randn(20)).reshape(5,4)
for n in list(range(1,6)):
    print(n,'행 합계 : ',np.sum(aa[n-1,:]))
    print(n, '행 최댓값 : ',np.max(aa[n-1,:]))


# step2 : indexing 관련문제
# 문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
bb = np.zeros((6,6))
print(bb)

# 조건1> 36개의 셀에 1~36까지 정수 채우기
k = 1
for i in range(0,6):
    for j in range(0,6):
        bb[i,j] = k
        k += 1
        
# 조건2> 2번째 행 전체 원소 출력하기 
print(bb[1,:]) 

# 조건3> 5번째 열 전체 원소 출력하기
print(bb[:,4])

# 조건4> 15~29 까지 아래 처럼 출력하기
print(bb[2:5,2:5])

# 문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.
cc = np.zeros((6,4))
print(cc)

# 조건1> 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 난수 정수를 저장하고,
#       두 번째 열부터는 1씩 증가시켜 원소 저장하기
import random
for i in range(0,6):
    q = random.randint(20, 100)
    for j in range(0,4):
        cc[i,j] = q
        q += 1
print(cc)

# 조건2> 첫 번째 행에 1000, 마지막 행에 6000으로 요소값 수정하기
cc[0,:] = 1000
cc[5,:] = 6000
print(cc)

# step3 : unifunc 관련문제
# 표준정규분포를 따르는 난수를 이용하여 4행 5열 구조의 다차원 배열을 생성한 후
# 아래와 같이 넘파이 내장함수(유니버설 함수)를 이용하여 기술통계량을 구하시오.
# 배열 요소의 누적합을 출력하시오.

dd = np.random.randn(20).reshape(4, 5)
print(dd)
print('평균 : ',np.average(dd))
print('합계 : ',np.sum(dd))
print('표준편차 : ',np.std(dd))
print('분산 : ',np.var(dd))
print('최댓값 : ',np.max(dd))
print('최솟값 : ',np.min(dd))
print('1사분위 수 : ',np.percentile(dd,25))
print('2사분위 수 : ',np.percentile(dd,50))
print('3사분위 수 : ',np.percentile(dd,75))
print('요소값 누적합 : ',np.cumsum(dd))