# 반복문 for
# 웹에서 읽은 자료라 가정 : 단어 수 출력 ex) 모터를:3
ss = """김 원내대표는 29일 국회에서 열린 원내대책회의 후 기자들과 만나 "더불어민주당에서 원내지도부를 새로 
개편하면서 그에 따라 우리도 새로 (원내지도부를) 개편할 필요성이 생겼고, 새 정부의 여러 법률안, 인사청문회, 국회임명동의안 처리 등이 4월 
중 지속되는데 업무의 연속성 측면에서 원내대표를 조기에 새로 뽑아야 여야 협상 진행이 효율적일 것"이라며 이같이 밝혔다.
그는 "여야 협상 과정에서 우리 당이 원내대표 선출 선거 국면으로 들어가면 (새 정부 출점 준비를 위한) 업무에 차질이 생긴다"며
 "(제가) 조금 일찍 임기를 마치고 새 원내대표를 뽑는 게 순리라 판단했다"고 부연했다.
김 원내대표 임기는 4월30일까지다. 그러나 4월 초 지명 예정인 국무총리 후보자의 인준안 처리와 4월 중순께 국회로 넘어올 
정부조직법 개정안 협상 등이 통상 1개월 이상 걸리는 점을 감안할 때 새 원내대표를 선출해 협상에 임하도록 하는 것이 맞다고 판단해 조기 사퇴를 결심한 것이다.
"""

import re

ss2 = re.sub(r'[^가-힣\s]', '', ss)   #한글과 공백만 표시
print(ss2)
ss3 = ss2.split(sep=' ')
print(len(ss3))
print(len(set(ss3))) #set type으로 바꿔 중복 제거

cou = {} # 단어의 발생 횟수를 dict로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1 # {'키' :i}
print(cou)

print()
for test in ['111-1234', '일이삼-사오육칠', '2222-3333']:
    if re.match(r'^\d{3,4}-\d{4}$', test):
        print(test)
    else:
        print('전화번호 ㅠㅠ')
        
print()
a = 1,2,3,4,5,6,7,8,9,10
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
        
print(li)

print(list(i for i in a if i % 2 == 0))

print()
datas = [1,2,'a',True, 3.4]
li = [i for i in datas if type(i) == int]
print(li)

print()
datas = {1,1,2,2,3}
se = {i * i for i in datas}
print(se)

print()
id_name = {1:'tom', 2:'james'}
name_id = {value:key for key, value in id_name.items()}
print(name_id)

print()
temp = [1, 2, 3]
for i in temp:
    print(i, end = ' ')
print()
print([i for i in temp])
print({i for i in temp})

print()
# 과일 값 계산
price = {'사과':2000, '오렌지':1000, '배':3000}
guest = {'사과':2, '배':1}
bill = sum(price[f] * guest[f] for f in guest)  # sum(요소들) : 합을 구하는 내장 함수
print(bill)




