# 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.
"""
*
**
***
****
*****
******
*******
********
*********
**********
"""
for i in range(0, 10):
    for j in range(0, i + 1):
        print('*', end='')
    print('')

# 역삼각형

for i in range(10, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print('')

# 별해
for i in range(1, 11):
    print('*' * i)