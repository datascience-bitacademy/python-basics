# 생성
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

d2 = {}
print(d2, type(d2))

d3 = dict()
print(d3, type(d3))

d4 = dict(one=1, two=2, three=3, four=4)
print(d4, type(d4))

d5 = dict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
print(d5, type(d5))

# index 대신에 key로 값(데이터)에 접근한다.
print(d['basketball'])

# 크기
print(len(d))

# in, not in : key의 존재 여부
print('soccer' not in d)
print('baseball' in d)

# 다양한 타입의 key를 사용할 수 있다.
d6 = {}
print(d6)

d6['twenty'] = 20    # str
d6[True] = 'true'    # bool
d6[10] = 10           # int
print(d6)

# 키는 변경불가능한 타입의 값을 사용해야 한다.
# d6[[1, 2, 3]] = 6
d6[(1, 2, 3)] = 6

print("=============객체함수===================")

# keys()
k = d6.keys()
print(k, type(k))
for key in k:
    print(key, d6[key])

# values()
v = d6.values()
print(v, type(v))
for value in v:
    print(value)

# items()
items = d6.items()
print(items, type(items))
for item in items:
    print(item)

phones = {'마이콜': '000-0000-0000', '둘리': '111-1111-1111', '또치': '222-2222-2222'}
print(phones['둘리'])
print(phones.get('둘리'))

# get(): 객체 함수를 사용하는 이유: 값 객체가 없는 경우 None을 반환 받을 수 있기 때문에...
# print(phones['도우넛'])
v = phones.get('도우넛')
if v is None:
    print('도우넛 키를 가진 값은 없습니다.')

# setDeafualt(): get()와 차이점은 존재하지 않는 경우 Deault 값이 저장된다.
v = phones.setdefault('둘리', '555-5555-5555')
print(v)
v = phones.setdefault('도우넛', '555-5555-5555')
print(v)

print(phones)

# pop() : 삭제와 동시에 값을 가져온다.
v = phones.pop('둘리')
print(v)
print(phones)

# popitem(): 삭제와 동시에 (키, 값) 가져온다.
item = phones.popitem()
print(item)
print(phones)

# clear()
phones.clear()
print(phones)

# 조회
d7 = {'c': 3, 'a': 1, 'b': 2}

for key in d7:
    print(key, end=' ')
else:
    print('')

for key in d7.keys():
    print(key, end=' ')
else:
    print('')

for key, value in d7.items():
    print(key, value)


