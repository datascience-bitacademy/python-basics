# 복소수: 실수부 + 허수부(j, J를 붙힌다)

a = 4 + 5j
print(a, type(a))

# 복소수 연산
b = 7 - 2j
print(a + b)

print(b, "의 실수부:", b.real)
print(b, "의 허수부:", b.imag)
print(b, "의 켤레복소수:", b.conjugate())

