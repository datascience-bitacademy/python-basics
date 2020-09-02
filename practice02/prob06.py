import random

while True:
mi, ma = 1, 100

n = random.randrange(ma) + mi
print('수를 결정 하였습니다. 맞춰보세요')
while True:
    print(mi + "-" + ma)
    s = input('>>')
    break


