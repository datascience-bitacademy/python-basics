a = 23
a = 20 + 3

print(a, type(a))
print(isinstance(a, int))

# 2진수, 10진수, 8진수, 16진수
b = 0b1101
c = 0o23
d = 0x23
print(b)
print(c)
print(d)

# 3.x에서는 int, long 합쳐졌다. 따라서 표현범위가 무한대이다.
e = 2**1024
print(e, type(e))
print(e.bit_length())

# 변환함수
print(bin(38))
print(oct(38))
print(hex(38))


