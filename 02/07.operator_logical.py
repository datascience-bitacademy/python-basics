
# 일반적으로 피연산자(operand)는 Triue 또는 False 값을 가지는 연산
a = 20

# not T  = F
# not F  = T
print(not a < 20)

#  T and T = T
#  T and F = F
#  F and T = F
#  F and F = F
print(a < 30 and a != 30)

#  T or T = T
#  T or F = T
#  F or T = T
#  F or F = F
print(a == 30 or a > 30)

# 논리식의 계산순서
print(True or bool('logical'))
print(True or 'logical')
print(False or 'logical')
print([] or 'logical')
print([] and 'logical')
print([2, 10] and 'logical')


def f():
    print('hello world')


a = 20
# if a > 10:
#     f()
a > 10 or f()

s = 'Hello World'
s and print(s)

