def func1(a):
    x = 10
    return a + x


def func2(a):
    return a + x


def func3(a):
    global g
    g = 3
    return a + g


x = 1
g = 10

# (L)GB
r = func1(10)
print(r)
print(x)

# L(G)B
r = func2(10)
print(r)

# LG(B)
print(dir('__builtins__'))

# global 키워드
r = func3(10)
print(r)
