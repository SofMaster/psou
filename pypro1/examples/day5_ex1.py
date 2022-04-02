# https://cafe.daum.net/flowlife/RUrO/24 example) 3

# 다중 상속
class Animal:
    def move(self):
        pass

class Dog(Animal):
    name = ' 개'
    
    def move(self):
        print(' 개는 낮에 돌아 다님')
        
        
class Cat(Animal):
    name = ' 냥이'
    
    def move(self):
        print(' 고양이는 밤에 돌아 다님')
        print(' 눈빛이 빛남')
        
class Wolf(Dog, Cat):
    pass

class Fox(Cat, Dog):
    def move(self):
        print('나는 여우')
        
    def foxMethod(self):
        print('여우의 고유 메소드')
        
        
dog = Dog()
print(dog.name)
dog.move()

print()
cat = Cat()
print(cat.name)
cat.move()

print()
wolf = Wolf()
wolf.move()

print()
print(Wolf.__mro__)