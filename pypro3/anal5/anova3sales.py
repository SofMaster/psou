# data.go.kr 사이트에서 어느 음식점 매출데이터와 날씨 데이터를 이용하여 강수 여부에 따른 매출액 평균에 차이를 검정

# 비가 올 때의 매출액
# 비가 안올 때의 매출액

# 귀무 : 강수량에 따른 매출액에 차이가 없다.
# 대립 : 강수량에 따른 매출액에 차이가 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats

# 자료 읽기1
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tsales.csv",
                         dtype = {'YMD' : 'object'})
print(sales_data.head(3))
print(sales_data.info())
print()
# 자료 읽기2
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-',''))  # 2018-06-01 => 20180601
print(wt_data.head(3))
print(wt_data.info())

print()
# 두 파일을 병합
frame = sales_data.merge(wt_data, how = 'left', left_on = 'YMD', right_on = 'tm')
print(frame.head(5))
print(len(frame))
print(frame.columns)

data = frame.iloc[:,[0, 1, 7, 8]] # 'YMD', 'AMT', 'maxTa', 'sumRn'
print(data.head(3), len(data))
print(data.isnull().sum()) # 결측치 없음

print()
# 이렬 최고온도를 구간 설정
print(data.maxTa.describe())
import matplotlib.pyplot as plt
#plt.boxplot(data.maxTa)
#plt.show()

data['ta_gubun' ] = pd.cut(data.maxTa, bins =[-5, 8, 24, 38], labels=[0,1,2])
print(data.head(3), ' ', data['ta_gubun'].unique())

# 상관분석
print(data.corr())
x1 = np.array(data[data.ta_gubun == 0].AMT)
x2 = np.array(data[data.ta_gubun == 1].AMT)
x3 = np.array(data[data.ta_gubun == 2].AMT)
print(x1[:3])
print(x2[:3])

# 등분산성
print(stats.levene(x1,x2,x3).pvalue) # pvalue=0.039 < 0.05 등분산성 만족 x

# 정규성
print(stats.ks_2samp(x1,x2).pvalue)
print(stats.ks_2samp(x3,x2).pvalue)
print(stats.ks_2samp(x1,x3).pvalue) # 전부 만족 x

print()
spp = data.loc[: , ['AMT','ta_gubun']]
print(spp.groupby('ta_gubun').mean())

print(pd.pivot_table(spp,index=['ta_gubun'], aggfunc='mean'))
print(spp[:3])

sp = np.array(spp)
group1 = sp[sp[:,1]==0, 0]
group2 = sp[sp[:,1]==1, 0]
group3 = sp[sp[:,1]==2, 0]


f_statistic, pvalue = stats.f_oneway(group1,group2,group3) # 귀무가설 기각 --> 매출액은 온도에 영향이 있음
print('f_statistic : ',f_statistic)
print('pvalue : ', pvalue)

print()
# 정규성 만족 x
print(stats.kruskal(group1,group2,group3)) # kruskal-Wallis test
# pvalue 매우낮음 < 0.05 귀무가설 기가 매출액은 온도에 영향이 있음

print()
# 등분산성 만족 x
from pingouin import welch_anova
print(welch_anova(data=data,dv='AMT',between='ta_gubun'))
# 해석 : 날씨( 온도 : 더움, 보통, 추움)에 의해 매출액의 차이가 있다.

print()
# 사후 검정 (Post Hoc Test)
# 분산 분석은 세 개 이상의 집단에 평균에 차이 유무 만을 알려줌
# 세 개 이상의 집단 각각의 집단 간 평균의 차이를 알고 싶은 경우
from statsmodels.stats.multicomp import pairwise_tukeyhsd
turkey_result = pairwise_tukeyhsd(endog = spp['AMT'], groups = spp['ta_gubun'],alpha=0.05)
print(turkey_result)

turkey_result.plot_simultaneous(xlabel='mean',ylabel='group')
plt.show()