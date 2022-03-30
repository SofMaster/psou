# 함수 작성
a = 1
b = a + 1
# 어쩌구 저쩌구 하다가 모듈의 멤버로 함수 선언

def DoFunc1():
    print('DoFunc1 수행')
    
c = b + 20

# 함수 호출
DoFunc1() # 함수 호출
# 딴 짓 하다가...
res = DoFunc1() # 함수 호출
print(res)
print(DoFunc1())


# 함수도 객체이다.
print(DoFunc1)
print(id(DoFunc1)) # id() = 주소를 알려준다.
print(id(print))
print(id(sum))
print(id(c))

d = c             # 주소를 치환
DoFunc2 = DoFunc1 # 주소를 치환
DoFunc2()

print('-----')
def doFunc3(arg1, arg2):  # arg1, arg2 : 매개 변수
    res = arg1 + arg2 
    # return res
    if res % 2 == 1: #res가 홀수면 아무 값도 갖고가지 않고 짝수라면 res값을 들고간다.
        return
    else:
        return res

print('결과는 : ',doFunc3(10, 20))     # 10,20 : 파라미터
aa = doFunc3(10, 21)
print('결과는 : ',aa)

print('-----')
def area_tri(a,b):
    c = a * b / 2
    aria_print(c)       #함수는 함수를 call 할 수 있다.

def aria_print(c):
    print('삼격형의 면적은 ' + str(c))
    
area_tri(5,6)

print('-----')
def func1():    
    print('func1 멤버 처리')
    def func2():            # 내부 함수
        print('func2 멤버 처리 : 내부 함수')
    func2()
func1()


print('-----')
def swap(a,b):
    return b, a     # 여러개의 값이 반환되면 tuple로 반환된다.

a = 10; b = 20
c = swap(a,b)
print(c)
print(c[0], c[1])

print('-----')
# if 조건식 안에 함수 사용
def isOdd_func(arg):
    return arg % 2 == 1

mydict = {x:x * x for x in range(11) if isOdd_func(x)}
print(mydict)

print('*****************')
print('현재 파일(모듈)의 객체 목록 : ',globals()) # globals() : 객체 목록 호출

print('프로그램 종료')

