
i1 = 10
i2 = 20
print(hex(id(i1)), hex(id(i2)))

i1 = 1234567890
i2 = 1234567890
print(hex(id(i1)), hex(id(i2)))

i1 = 11
i2 = 10 + 1
print(hex(id(i1)), hex(id(i2)))

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

# is (동일 레퍼런스 비교)
# 가변 객체는 is(동일성)와 ==(동질성)는 다른 결과다. (list, set, dict)
# 불변 객체는 is(동일성)와 ==(동질성)는 같은 결과다. (나머지)
print(i1 is i2)
print(l1 is l2)
print(s1 is s2)

# ?
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 is t2)

# 형변환 함수는 불변 객체라고 하더라도 새로운 객체를 만든다. (바로 대입하는 = 와는 다르게 작동한다)
r = range(1, 4)
t3 = tuple(r)
print(t1 == t3)
print(t1 is t3)

# slicing 경우에도 불변 객체라고 하더라도 새로운 객체를 만든다. (바로 대입하는 = 와는 다르게 작동한다)
t4 = (0, 1, 2, 3)[1:]
print(t1 is t4)






