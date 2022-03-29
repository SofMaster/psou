# 정규표현식 : 대량의 문자열에 대해 일정한 패턴을 부여해 원하는 문자열만 취할 수 있다.
import re

ss = "1234 abc가나다abcABCfun_1235555_6'Python is fun"
print(ss)
print(re.findall('123', ss))
aa = re.findall(r'123', ss)
print(aa[0])
print(re.findall('가나', ss))
print(re.findall('[12]', ss))
print(re.findall('[0-9]', ss))
print(re.findall('\d\d', ss)) # \d = 글자수 \D \s \S \w \W
print(re.findall('[0-9]+', ss)) #meta문자
print(re.findall('[0-9]?', ss))
print(re.findall('[0-9]*', ss))
print(re.findall('[0-9]{2}', ss))
print(re.findall('[0-9]{2,3}', ss))
print(re.findall('[a-z]', ss))
print(re.findall('[a-zA-z]', ss))
print(re.findall('[가-힣]', ss))
print(re.findall('[^가-힣]', ss)) # 문자집합 안에서는 ^ = not과 같다.
print(re.findall('.bc', ss))
print(re.findall('a..', ss))
print(re.findall('^123', ss)) # 문자집합이 아니라면 ^ = ~로 시작되는과 같다.  
print(re.findall('fun$', ss)) # $ = ~로 끝나는
print(re.findall('12|34', ss)) #| = or
print(re.findall('(ab)+(c)', ss))

p = re.compile('abc')
print(re.findall(p,ss))

p = re.compile('the', re.IGNORECASE) # IGNORECASE = 대소문자 구분X
print(p.findall('The DoG the dog'))



