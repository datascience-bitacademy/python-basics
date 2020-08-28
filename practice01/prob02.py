# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

while True:
    i = input('정수를 입력 하세요:')

    if i == 'quit':
        break

    if i.isdigit() is False:
        break

    print('짝수' if int(i) % 2 == 0 else '홀수')
