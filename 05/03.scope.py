def func1(a):
    x = 10 # 할당 작업 -> 로컬 심볼 테이블에 생성
    return a + x


def func2(a):
    return a + x # x는 할당이 일어나지 않음 -> Global 영역의 x를 참조


def func3(a):
    # global g
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
