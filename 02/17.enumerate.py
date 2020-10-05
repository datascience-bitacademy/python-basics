# enumerate() 함수 사용하기

index = 0
for color in ['red', 'yellow', 'blue', 'black', 'gray']:
    # 내부 값은 알 수 있지만, 실제 인덱스는 모른다
    print(index, color)
    index = index + 1

# enumerate 함수로 묶으면 (인덱스, 값)의 튜플로 전달
for item in enumerate(['red', 'yellow', 'blue', 'black', 'gray']):
    print(item[0], item[1])

for index, color in enumerate(['red', 'yellow', 'blue', 'black', 'gray']):
    # 전달받은 튜플을 언패킹
    print(index, color)
