# 상속

class Person:
    say = '난 사람이야'
    nai = 20
    __abc = 'good' # __변수명 : private (현재 class에서만 유효한 변수)
    
    def __init__(self,nai):
        print('Person 생성자')
        self.nai = nai
        
    def printInfo(self):
        print('나이 : {}, 이야기 : {}'.format(self.nai, self.say))
        
    def hello(self):
        print('안녕')
        print(self.__abc)
    
    @staticmethod   #staticmethod : 어디서든 자유롭게 부를 수 있다, self가 없어도 된다.
    def sbs(tel):
        print('sbs _ static Method', tel)   
        
print(Person.say, Person.nai)
p = Person(22)
p.printInfo()
p.hello()

print('***' * 10)
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'
    def __init__(self):
        print('Employee 생성자 ~~~')
    
    def printInfo(self):    # method override
        print('Employee 클래스 내의 printInfo')
    
    def eprintInfo(self):
        self.printInfo()
        super().printInfo()
        print(self.say, super().say)
        
e = Employee()
print(e.say, e.nai)
print(e.subject)
e.eprintInfo()
e.printInfo()

print('---' * 10)
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)   # Bound method call
    
    def wprintInfo(self):
        super().printInfo()
        
w = Worker('25')
print(w.say, w.nai)
w.printInfo()
w.wprintInfo()

print('~~~' * 10)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        Worker.__init__(self, nai)  #unBound method call
        
    def wprintInfo(self): # method Overriding
        print('Programmer 내에 작성된 wprintinfo')
    
    def hello2(self):
        print(super.__abc)
pr = Programmer(33)
print(pr.say, pr.nai)
pr.printInfo()
pr.wprintInfo()

print()
p.hello()
# p.hello2() private 참조 X
w.sbs('111-1111')
pr.sbs('222-2222')

print('클래스 타입---')
a = 10
print(type(a))
print(type(pr))
print(Programmer.__bases__)
print(Worker.__bases__)
print(Person.__bases__)