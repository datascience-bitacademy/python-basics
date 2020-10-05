# range() 함수 사용
# range(start=0, end, step=1)

seq = range(10) # == range(0, 10, 1) - 0 ~ 9까지의 정수자료
print(seq, type(seq))

for i in seq:
    print(i, end=' ')
else:
    print('')

for i in range(5, 15): # 5 ~ 14까지
    print(i, end=' ')
else:
    print('')


for i in range(0, -10, -1): # 0 ~ -9까지 역순
    print(i, end=' ')
else:
    print('')

for i in range(0, 10, 2): # 0 ~ 9까지 2간격으로
    print(i, end=' ')
else:
    print('')

