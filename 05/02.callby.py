# 파이썬은 call by reference 이다.
# 하지만, 함수 내부에서 값을 변경하더라도 값이 변경되지 않는다.


def f1(p):
    p = 100


def f2(seq):
    seq[0] = 0


a = 10
f1(a)
print(a)


# 파라미터가 sequence type(immutable)인 경우
# 내부 변경시 오류가 발생한다.
# a = (1, 2, 3)
# f2(a)

# 파라미터가 sequence type(mutable)인 경우
a = [1, 2, 3]
f2(a)
print(a)

