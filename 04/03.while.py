# 1 ~ 10 합을 구하기
s, count = 0, 1
while count < 11:
    s += count
    count += 1
print(s)

# break
i = 0
while i < 10:
    if i > 5:
        break
    print(i, end=' ')
    i += 1

print("\n-------------------------------")

# continue
i = 0
while i < 10:
    if i <= 5:
        i += 1
        continue
    print(i, end=' ')
    i += 1

print('\n-------------------------------')

# 무한루프
i = 0
while True:
    print(i, end=' ')

    if i > 5:
        break

    i += 1
