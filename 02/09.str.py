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

# str 역시 순차자료형의 특징 가지고 있다
# 불변 객체 -> 내부 값은 변경할 수 없다
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
# print("hello" + 2) # Error
print('hello' + str(2))

# 인덱싱(sequence 타입이 가지는 특징)
#    F   i  r  s  t     S  t  r  i  n   g
#    0   1  2  3  4  5  6  7  8  9  10  11(== len(s1))
#  -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2  -1
print(s1[0], s1[1], s1[2]) # 정방향 indexing
print(s1[-12], s1[-11], s1[-10]) # 역방향 indexing

# slicing(sequence 타입이 가지는 특징)
s7 = s1[2:5] # [시작:끝경계:간격]
print(s7) # rst
print(s1[-10:-7]) # 음수 인덱스 이용한 슬라이싱
print(s7 == s1[-10:-7])
print(s1[2:]) # == s1[2:len(s1)] -> 생략하면 끝까지

# 슬라이싱의 세 번째 값은 간격값(기본 1)
print("간격 2:", s1[::2]) # 처음부터 끝까지 간격을 2로 == s1[0:len(s1):2]
# 간격값이 음수면 방향이 반대
print("간격 -1:", s1[::-1])

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
print("name: {}, age: {}".format(name, age))    # 익명 플레이스홀더
print("name: {0}, age: {1}".format(name, age))  # numbered placeholder
print("name: {1}, age: {0}".format(age, name))
print("name: {n}, age: {a}".format_map({'n': name, 'a': age})) # named placeholder
# 사전을 포맷할 때는 format_map 메서드 활용

print('======== 객체함수 =======')
# 대소문자
s8 = 'i like Python'
print(s8.upper())
print(s8.lower())
print(s8.swapcase()) # 대문자 <-> 소문자
print(s8.capitalize()) # 첫 글자만 대문자, 나머지는 소문자
print(s8.title()) # 각 단어의 첫 글자만 대문자
# 검색
s9 = 'I Like Python, I Like Java Also'
print(s9.count('Like'))
print(s9.find('Like')) # 처음부터 검색
print(s9.find('Like', 5)) # 검색 범위 제한
print(s9.find("Like", 21)) # -1 : 없다

print(s9.find('JavaScript'))
print(s9.rfind('Like'))
print(s9.startswith('I Like'))
print(s9.startswith('I Like', 2))
print(s9.endswith('Also')) # Also로 끝나는가?
print(s9.endswith('Java', 0, 26)) # 범위의 제한 [0:26] 구간의 문자열이 Java로 끝나는가

# find와 index :-> 사용법은 거의 동일
# find는 예외 발생 없음
# index는 예외 발생

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
print('-------' + s10.strip() + '------') # 양 끝의 화이트 스페이스 제거
print('-------' + s10.rstrip() + '------')  # 오른쪽 끝의 화이트 스페이스제거
print('-------' + s10.lstrip() + '------')  # 왼쪽 끝의 화이트 스페이스 제거

s11 = '<><abc><><defg><>'
print('-------' + s11.strip('<>') + '------')   # 지정한 문자(< or >)

s12 = 'Hello Java Java Java'
print('-------' + s12.replace('Java', '') + '------') # 내부의 검색어 Java를 다른 문자열로 치환

# 정렬
s13 = 'King and Queen'
print('---' + s13.center(30) + '---') # 30자리 확보 후 문자열을 가운데 정렬
print('---' + s13.ljust(30) + '---')    # 30자리 확보 후 문자열을 왼쪽 정렬
print('---' + s13.rjust(30) + '---')    # 30자리 확부 후 문자열을 오른쪽 정렬

# 분리
s14 = 'spam and ham'
r = s14.split(' and ') # 구분자를 기준으로 문자열을 분절 -> list 반환
print(r, type(r))

s15 = 'one:two:three:four'
r = s15.split(':')
print(r)

r = s15.split(':', 2) # 왼쪽 두개, 나머지 -> 3개 요소의 list
print(r)

r = s15.rsplit(':', 2) # 나머지, 오른쪽 두 개 -> 3요소의 list
print(r)

lines = '''1st line
2nd line
3rd line
4th line
'''
r = lines.strip().split('\n')
print(r)

r = lines.splitlines() # lines.split('\n')
print(r)

# 결합
s16 = '&'.join(r)   # 문자열을 기준으로 리스트를 연결하여 새 문자열 반환
print(s16)

# 판별
print("1234".isdigit())
print("abcd".isalpha())
print("1234".isalpha())
print("abcd".isdigit())
print("abcd".islower())
print("ABCD".isupper())
print(" ".isspace()) # 화이트 스페이스 확인 : 공백, 개행, 탭문자
print("".isspace())
print("\n".isspace())
print("\t".isspace())

#  '0' 채우기
number = 234
print(str(number).zfill(5)) # 5자리 빈 공간 확보하고 문자열 세팅 후, 왼쪽 빈 공간에 0을 채운다


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

# docstring

def docstr():
    """
    파이썬은 모듈의 상단,
    클래스, 함수의 선언부 바로 아래 간단한 설명을 적으면
    docstring이 된다"""

# docstring의 확인 : 객체.__doc__
print(docstr.__doc__)
# docstring은 help 함수로도 확인
help(docstr)