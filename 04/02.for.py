# for ~반복문
# for o in [sequnce 객체] :
for number in [10, 20, 30, 40]:
    result = number**2
    print(result, end=' ')
else:
    print('\n------------------------')


a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end=' ')
else:
    print('\n------------------------')

# 복합 자료형을 for문에서 사용하는 경우
l = [('둘리', 10), ('마이콜', 30), ('또치', 11)]
for t in l:
    print('이름: %s, 나이:%d' % t)

# 10번 반복하는 Loop
for i in range(0, 10):
    print(i, end=' ')
else:
    print('\n------------------------')

# 1 ~ 10 합을 구하기
s = 0
for n in range(1, 11):
    s += n
print(s)

# break
for n in range(10):
    if n > 5:
        break
    print(n, end=' ')

# break
for n in range(10):
    if n > 5:
        break
    print(n, end=' ')
else:
    print('정상루프 종료')

print("\n--------------------------")

# break
for n in range(10):
    if n <= 5:
        continue
    print(n, end=' ')
else:
    print('\n--------정상루프 종료---------')

for i in range(1, 10):
    for j in range(1, 10):
        print("%d X %d = %d" % (i, j, i*j))

    print("----------------------")

