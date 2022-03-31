# 클래스는 새로운 타입을 만든다.
from string import printable
class Singer:
    title_song = '화이팅 코리아' 
    
    def sing(self):
        msg = '노래는'
        print(msg, self.title_song, '랄라라 ~~~')
    
    def hello(self):
        print('안녕하세요 저 가수에요')    
    # ...
    
    
# -------- 아래 내용은 별도의 모듈을 만들었다. ----------
bts = Singer()   #class명() () = 생성자
bts.sing()
bts.hello()

print()
blackpink = Singer()
blackpink.hello()
blackpink.sing()
blackpink.title_song = '마지막처럼'
blackpink.sing()
blackpink.co = 'SM'
print('blackpink 소속사 : ', blackpink.co)

#print('bts 소속사 : ', bts.co)
bts.sing()

print()
print(id(bts), id(blackpink))
print(type(bts), type(blackpink))