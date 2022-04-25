
import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd

url = "http://www.kyochon.com/menu/chicken.asp"
kyochon = req.urlopen(url)  
soup = BeautifulSoup(kyochon,'lxml')
ss = soup.select(".menuProduct .money>strong")
dd = soup.select(".menuProduct .txt>dt")
list1 = []
list2 = []
for d in dd:
    if d.string != None:
        list1.append(d.string)
for s in ss:
    if s.string != None:
        tmp = s.text.strip()
        tmp = tmp.replace(',','')
        list2.append(int(tmp))
        
df1 = pd.DataFrame(data=list1,columns = ['상품명'])
df2 = pd.DataFrame(data=list2)
df1['가격'] = df2
print(df1['가격'].mean())
print(df1['가격'].std())