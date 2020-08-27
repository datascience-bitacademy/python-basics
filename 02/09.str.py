# 한 줄 문자열
s = ''
str1 = 'Hello World'
str2 = "Hello World"
print(type(s), type(str1), type(str2))
print(isinstance(str1, str))

# 여러 줄 문자열
str3 = '''ABC
DEF
가나다라마바사
아자차카타파하'''
print(str3)

# 여러줄 주석 -> 여러 줄 문자열
'''
주석1
주석2
주석3
'''

# escape
print('hello\nworld\n')
print("hello \"world\"")
print('She\'s Mom')
print("She's Mom")
print("둘리\t010-0000-0000")

print('====== 문자열 연산 =======')
s1 = 'First String'
s2 = 'Second String'

# 반복
s3 = s1*3
print(s3)

# +(연결. concatenate)
s4 = s1 + ' ' + s2
print(s4)
s5 = 'Hello' + '-' + 'world'
s6 = 'Hello' '-' 'world'   # + 생략 가능하다.
print(s6)

# 문자열 객체와 정수 객체는 연결(+) 연산을 할 수 없다.
# 예외: 발생
# print("hello" + 2)
print('hello' + str(2))

# 인덱싱(sequence 타입이 가지는 특징)
#    F   i  r  s  t     S  t  r  i  n   g
#    0   1  2  3  4  5  6  7  8  9  10  11
#  -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1
print(s1[0], s1[1], s1[2])
print(s1[-12], s1[-11], s1[-10])

# slicing(sequence 타입이 가지는 특징)
s7 = s1[2:5]
print(s7)
print(s1[2:])

# len() 함수(sequence 타입이 가지는 특징)
print(len(s1))

# in, not in 연산자(sequence 타입이 가지는 특징)
print("s" in s2)
print("s" not in s2)

print('====== 포맷팅 =======')
# tuple
print("name: %s, age: %d" % ('둘리', 10))

# format() 함수
name = '마이콜'
age = 30
print("name: " + format(name, 's') + ",age: " + format(age, 'd'))

print('======== 객체함수 =======')
s8 = 'i like Python'
print(s8.upper())
print(s8.lower())
print(s8.swapcase())
print(s8.capitalize())
print(s8.title())

s9 = 'I Like Python, I Like Java Also'
print(s9.count('Like'))
print(s9.find('Like'))
print(s9.find('Like', 5))
print(s9.find('JavaScript'))
print(s9.rfind('Like'))

# str 객체는 변경할 수 없다(불변성, Immutable)
# s10 = 'hello'
# s10[0] = 'f'
# print(s10)

# [cf] list는 변경 가능하다(mutable)
l1 = ['hello', 'world']
print(l1)
l1[0] = 'HELLO'
print(l1)
l1.append('Python')
print(l1)

