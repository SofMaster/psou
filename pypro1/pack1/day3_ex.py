# https://cafe.daum.net/flowlife/RUrO/40
'''
 함수 처리
 연습문제) 키보드를 통해 직원 자료를 입력받아 가공 후 출력하기
 함수를 두 개 작성
  datas = inputfunc() : 키보드로 값을 입력 받아 datas 변수에 담는 역할
                        while True: 문으로 무한루핑하며, 계속입력할까요?n이 될 때까지 자료를 입력받는다.
  processfunc(datas) : datas에 기억된 내용을 출력한다.
  
  처리 조건 :급여액은 기본급 + 근속수당 
          수령액은 급여액 – 공제액

근무년수에 대한 수당표
근무년수    0~3년    4~8년    9년이상
근속수당    150000  450000  1000000

급여 상한액에 대한 공제세율표
급여액    300만원 이상    200만원 이상    200만원 미만
공제세율     0.5            0.3          0.15  
'''
def inputfunc():
    tmp = 1
    while True:
        print('사번,이름,기본급,입사년도를 입력하세요')
        data = list(input().split(","))
        processfunc(data)
        
        yn = input('계속 하시겠습니까? y/n : ')
        if yn == 'y':
            tmp +=1
            continue
        else:
            print('처리한 건수 : {}건'.format(tmp))
            break
        

def processfunc(data):
    num,name,income,year = data
    a = 2022 - int(year)
    bonus = 0
    tax= 0
    if a>=9:
        bonus = 1000000
    elif a>=4:
        bonus = 450000
    else:
        bonus = 150000
               
    total = int(income)+bonus
    if total >= 3000000:
        tax=0.5
    elif total >= 2000000:
        tax=0.3
    else:
        tax= 0.15
           
    print('{} {} {} {} {} {} {}'.format(num,name,income,a,bonus,total*tax,total-total*tax))

inputfunc()

            
