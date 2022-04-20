# 시각화 : 많은 양의 데이터를 효율적으로 봄으로해서 인사이트를 정확하게 얻어 낼 수 있다 ...

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

x = ["서울","인천","수원"]  # set은 순서가 없기 때문에 안된다. tuple list 가능
y = [5, 3, 7]

# plt.plot(y)
# plt.xlim([-1, 3])  # x축 경계값 지정
# plt.ylim([0, 10])  # 축 경계값 지정
# plt.yticks(list(range(0,11,3)))
# plt.plot(x, y)
# plt.show()

data = np.arange(1, 11, 2)
print(data)
plt.plot(data)
x = [0,1,2,3,4]
for a, b in zip(x, data):
    plt.text(a,b,str(b))
plt.show()

# sin 곡선
x = np.arange(10)
y = np.sin(x)
print(x, y)
# plt.plot(x, y)
# plt.plot(x,y,'bo')
# plt.plot(x, y, 'r+')
plt.plot(x, y, 'go--',linewidth = 2, markersize = 12)  # lw=2, marker = 'o', c = 'g'
plt.show()

# hold
x = np.arange(0, np.pi * 3, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize = (10, 5))
plt.plot(x, y_sin, 'r')
plt.scatter(x,y_cos)   # 산점도
plt.xlabel('x축')
plt.ylabel('Y축')
plt.legend(['sine', 'cosine'])  # 범례
plt.show()

# subplot  #figure를 쪼개기
plt.subplot(2, 1, 1)  # 2행 1열 focus = 1행
plt.plot(x, y_sin, 'r')
plt.title('사인 그래프')
plt.subplot(2, 1, 2)  # 2행 1열 focus = 2행
plt.scatter(x,y_cos)
plt.title('코사인 그래프')
plt.show()

# 꺽은 선 그래프
irum = ['a','b','c','d','e']
kor = [80, 50, 70, 70, 90]
eng = [60, 70, 80, 70, 60]
plt.plot(irum, kor, 'ro-')
plt.plot(irum, eng, 'bs-.')
plt.title('시험점수')
plt.ylim([0, 100])
plt.legend(['국어', '영어'], loc = 4)    # 시계 반대방향으로 1,2,3,....
plt.grid(True)

fig = plt.gcf()  # 그래프를 이미지로 저장
plt.show()
fig.savefig('plot1.png')

from matplotlib.pyplot import imread
img = imread('plot1.png')
plt.imshow(img)
plt.show()
plt.show()