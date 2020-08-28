# range() 함수 사용

seq = range(10)
print(seq, type(seq))

for i in seq:
    print(i, end=' ')
else:
    print('')

for i in range(5, 15):
    print(i, end=' ')
else:
    print('')


for i in range(0, -10, -1):
    print(i, end=' ')
else:
    print('')

for i in range(0, 10, 2):
    print(i, end=' ')
else:
    print('')

