# 사칙연산
print(2 * 3)
print(2 + 3)
print(2 - 3)
print(2 / 3)
print(2 / 3.0)
print(2.0 / 3.0)

# //(몫연산자), **(지수승), %(나머지 연산자)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# divmod() 함수
t = divmod(2, 3)
print(t, type(t))

# 산술 연산자 우선순위
#  1. +, - (단항 연산자)
#  2. **
#  3. *, / , %, //
#  4. +, - (이항 연산자, 더하기/빼기)
print(2 + 3 * 4)
print(-(2 + 3) * 4)

# 결합순서
print(2 ** 3 ** 4)
print(2 ** (3 ** 4))
print((2 ** 3) ** 4)


