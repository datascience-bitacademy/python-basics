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

# dict
print("name: %(name)s, age: %(age)d" % {'age': 10, 'name': '둘리'})

# format() 함수
name = '마이콜'
age = 30
print("name: " + format(name, 's') + " ,age: " + format(age, 'd'))

# format() 객체 함수
print("name: {}, age: {}".format(name, age))
print("name: {0}, age: {1}".format(name, age))
print("name: {1}, age: {0}".format(age, name))
print("name: {n}, age: {a}".format_map({'n': name, 'a': age}))

print('======== 객체함수 =======')
# 대소문자
s8 = 'i like Python'
print(s8.upper())
print(s8.lower())
print(s8.swapcase())
print(s8.capitalize())
print(s8.title())
# 검색
s9 = 'I Like Python, I Like Java Also'
print(s9.count('Like'))
print(s9.find('Like'))
print(s9.find('Like', 5))
print(s9.find('JavaScript'))
print(s9.rfind('Like'))
print(s9.startswith('I Like'))
print(s9.startswith('I Like', 2))
print(s9.endswith('Also'))
print(s9.endswith('Java', 0, 26))
try:
    print(s9.rindex('Like'))
    s9.index('JavaScript')
except ValueError as ex:
    print('index()는 발견하지 못하면 예외가 발생한다.')
    # 예외
    # 1. 로그를 남긴다.
    # 2. 사용자한테 사과.
    # 3. 정상종료

# 편집과 치환
s10 = '  spam and ham   '
print('-------' + s10.strip() + '------')
print('-------' + s10.rstrip() + '------')
print('-------' + s10.lstrip() + '------')

s11 = '<><abc><><defg><>'
print('-------' + s11.strip('<>') + '------')

s12 = 'Hello Java Java Java'
print('-------' + s12.replace('Java', '') + '------')

# 정렬
s13 = 'King and Queen'
print('---' + s13.center(30) + '---')
print('---' + s13.ljust(30) + '---')
print('---' + s13.rjust(30) + '---')

# 분리
s14 = 'spam and ham'
r = s14.split(' and ')
print(r, type(r))

s15 = 'one:two:three:four'
r = s15.split(':')
print(r)

r = s15.split(':', 2)
print(r)

r = s15.rsplit(':', 2)
print(r)

lines = '''1st line
2nd line
3rd line
4th line
'''
r = lines.split('\n')
print(r)

r = lines.splitlines()
print(r)

# 결합
s16 = '&'.join(r)
print(s16)

# 판별
print("1234".isdigit())
print("abcd".isalpha())
print("1234".isalpha())
print("abcd".isdigit())
print("abcd".islower())
print("ABCD".isupper())
print(" ".isspace())
print("".isspace())
print("\n".isspace())
print("\t".isspace())

#  '0' 채우기
number = 234
print(str(number).zfill(5))


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

