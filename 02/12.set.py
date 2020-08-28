# 생성
s = {1, 2, 3}
print(s, type(s))

# 기본 연산
print(len(s))
print(2 in s)
print(10 not in s)

# list 중복성을 제거할 수 있다.
l = [1, 2, 3, 4, 2, 2, 5, 6, 5, 6]
s2 = set(l)
print(s2)

print("=============객체함수===================")
s3 = set()

s3.add(6)
print(s3)

s3.add(7)
print(s3)

s3.add(2)
print(s3)

s3.discard(2)
print(s3)

try:
    s3.remove(10)
except KeyError as e:
    print('remove는 discard와 다르게 존재하지 않는 항목 제거시 예외가 발생')

s3.remove(7)
print(s3)

s3.update({2, 4, 6})
print(s3)

s3.clear()
print(s3)

# 수학의 집합과 관련된 함수
s4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s5 = {10, 20, 30}

# 합집합
s6 = s4.union(s5)
print(s6)

# 교집합
s7 = s4.intersection(s5)
print(s7)

# 차집합
s8 = s4.difference(s5)
print(s8)

# 대칭차 집합
s9 = s4.symmetric_difference(s5)
print(s9)

