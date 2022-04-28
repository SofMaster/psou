# 두 집단 이하의 평균 또는 비율 차이 검정
# t 분포는 표본평균을 이용해 정규분포의 평균을 해석할 때 사용한다.
# 독립변수 : 범주형, 종속변수 : 연속형(평균이므로)

# 단일 모집단의 평균에 대한 가설검정(one samples t-test)
# 하나의 집단에 대한 표본평균이 예측된 평균(모집단의 평균)과 같은지를 검정.
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 연습 1) 어느 남성 집단의 평균 키는 177이다. (모집단의 평균키가 177이다). 남성 집단의 표본 데이터를 추출해 평균차이 검정
# 귀무 : 남성 집단의 평균 키는 177이다.
# 대립 : 남성 집단의 평균 키는 177이 아니다. (양측검정)
## 대립 : 남성 집단의 평균 키는 177 보다 크다(작다) (단측검정)

one_sample = [167.0, 182.7, 169.6, 176.8, 185.0]
print(np.array(one_sample).mean())  # 176.21999 vs 177 평균에 차이가 이는가?
# 데이터의 정규성 확인 (p - value 가 0.05보다 크므로 정규성 만족)
print(stats.shapiro(one_sample)) # ShapiroResult(statistic=0.921559751033783, pvalue=0.5400515794754028)

# 검정 수행
result = stats.ttest_1samp(one_sample, popmean = 177) # popmean = 모집단의 평균  
print('t값 : %.3f, p - value : %.3f'%result) # t값 : -0.221 p-value : 0.836
# 해석 : p - value:0.836 > 0.05 이므로 귀무가설 채택.

print()
result2 = stats.ttest_1samp(one_sample, popmean = 165) # popmean = 모집단의 평균  모집단의 평균 키가 165
print('t값:%.3f, p-value : %.3f'%result2)
# 해석 : p-value : 0.033 < 0.05 이므로 귀무가설 기각.

print('---------------------------')
# 실습 예제 2) A 중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리( 국어 점수 평균검정)
# A 중학교 1학년 1반 학생들의 국어 시험결과는 늘 80점이라고 알려져 있다.

# 귀무 : A 중학교 1학년 1반 학생들의 국어 시험결과의 평균은 80점이다.
# 대립 : A 중학교 1학년 1반 학생들의 국어 시험결과의 평균은 80점이 아니다.

data = pd.read_csv("../testdata/student.csv")
print(data.head(3))
print(data['국어'].mean())  # 72.9 vs 80 차이가 있느냐?
# print(data.describe())
print(stats.shapiro(data.국어)) # pvalue=0.01295 < 0.05 이므로 정규성 만족 X

print(stats.ttest_1samp(data.국어, popmean = 80))
# Ttest_1sampResult(statistic=-1.3321801667713213, pvalue=0.19856051824785262)
# pvalue=0.198560 > 0.05 이므로 귀무 채택. 수집된 데이터는 우연히 발생된 자료이다.

print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
# 실습 예제 2)
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는(단측 검정) 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.

# 귀무 : 여아 신생아 몸무게의 평균은 2800g 이다.
# 대립 : 여아 신생아 몸무게의 평균은 2800g보다 크다.

data = pd.read_csv("../testdata/babyboom.csv")
print(data.head(3), len(data))  # gender : 1 = 여아 , gender : 2 = 남아
fdata = data[data.gender == 1]
print(fdata.head(3), len(fdata))
print(np.mean(fdata.weight)) # 여아 몸무게의 평균 : 3132 vs 2800 차이?

# 정규성 확인
print(stats.shapiro(fdata.iloc[:, 2])) # pvalue=0.0179 < 0.05 이므로 정규성 만족 X 
print(stats.shapiro(fdata.weight))

# 시각화 정규성이 맞다면 종모양
sns.displot(fdata.iloc[:,2], kde = True) # kde : 밀도곡선 
plt.show()
 
stats.probplot(fdata.iloc[:,2], plot = plt) # Q-Q plot
plt.show()

print(stats.ttest_1samp(fdata.weight, popmean = 2800))
# test_1sampResult(statistic = 2.2331, pvalue = 0.0392 
# pvalue = 0.039 < 0.05 이므로 귀무가설을 기각하고 대립가설을 채택





