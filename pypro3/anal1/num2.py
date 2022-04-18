# numpy 기본 이해

import numpy as np

print(np.__version__)

s = 'tom' # scalar
ss = ['tom', 'james', 'oscar'] 
print(ss, type(ss))   # ['tom', 'james', 'oscar'] <class 'list'>
ss2 = np.array(ss)  
print(ss2, type(ss2))  # ['tom' 'james' 'oscar'] <class 'numpy.ndarray'>

print('\n------------------list/ndarray 기억상태 구분')
li = list(range(1, 10))
print(li)
print(id(li[0]), id(li[1]))   # 저장된 주소 : 3155795142960 3155795142992(다른 주소)
print(li * 10)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, ....]
print('-' * 10)

for i in li:
    print(i * 10, end = ' ')  # 10 20 30 40 50 60 70 80 90
    
print([i * 10 for i in li ])  # [10, 20, 30, 40, 50, 60, 70, 80, 90]

print()  # list to ndarray
num_arr = np.array(li)
print(num_arr)
print(id(num_arr[0]), id(num_arr[1]))  # 저장된 주소 : 3155842173456 3155842173456(같다)
print(num_arr * 10)

print()
# a = np.array([1, 2, '3.2'])  # ndarray는 type이 일치한다. 데이터는 상위 type을 따른다. int -> float -> complex -> str
a = np.array([1, 2, 3])
print(a, type(a), a.dtype, a.shape, a.ndim, a.size) # [1 2 3] <class 'numpy.ndarray'> int32 (3,) : 1차원 요소가 3개 1 3
print(a[0])  # 인덱싱
print(a[1:3])  # 슬라이싱
print(a[-1])  

print()
b = np.array([[1, 2, 3],[4, 5, 6]])
print(b, type(b), b.dtype, b.shape, b.ndim, b.size) # [1 2 3] <class 'numpy.ndarray'> int32 (3,) : 1차원 요소가 3개 1 3
print(b[0,])  # 인덱싱
print(b[1:3,])  # 슬라이싱
print(b[-1,])  
print(b[0, 0], b[1, 1])
print(b[[0]])

print()
c = np.zeros((2, 2))
print(c)

d = np.ones((1, 2))
print(d)

e = np.full((2,2), fill_value = 7)
print(e)

f = np.eye(3)  # 단위행렬 생성 대각만 1로 채우고 나머지는 0
print(f)

print()
print(np.random.rand(5), np.mean(np.random.rand(5)))  # 균등분포
print(np.random.randn(5), np.mean(np.random.randn(5))) # 정규분포 데이터의 갯수가 많아지면 0에 가까워짐

np.random.seed(1)
print(np.random.randn(2, 3))

print(np.random.randint(10, size = 6))       # 1차원
print(np.random.randint(10, size = (3,4)))   # 2차원
print(np.random.randint(10, size = (3,4,5))) # 3차원

print()
print(list(range(0, 10)))
print(np.arange(10))

print('-----인덱싱, 슬라이싱-----')
a = np.array([1, 2, 3, 4, 5])
print(a[1:5:2])   # 1부터 5까지 2씩 증가

a = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
print(a[:])
print(a[1:])
print(a[-1:])
print(a[0], a[0][0], a[0, 0], a[[0]])
print(a[1:, 0:2])

print()
b = a[:2, 1:3]  # 서브 배열
print(b)
print(b[0,0])
print(a[0,1])
b[0, 0] = 88
print(b)
print()
print(a)

c = a[:2, 1:3].copy()  # 배열 사본 복사 원본에는 영향을 미치지 않음
print(c)
c[0, 0] = 99
print(c)
print()
print(a)

print('---------------------')
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(a.shape)   # shape : 차원 행 열을 반환하는 함수 (3, 3)
r1 = a[1, :]
r2 = a[1:2, :]
print(r1, r1.shape)
print(r2, r2.shape)

print()
a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]])
print(a.shape)
print(a)
b = np.array([0, 2, 0, 1])  # a 배열 인덱싱용 배열 
print(b, b.shape)
print()
print(np.arange(4))
print(a[np.arange(4), b])

print()
bool_idx = (a > 10)  
print(bool_idx)

print(a[bool_idx])  # 참인 값만 출력
print(a[a > 10])    # 조건을 주고 출력할 수 있다.