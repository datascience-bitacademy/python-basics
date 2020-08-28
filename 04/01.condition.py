# if ~ else

a = 2
if a > 5:
    print('big')
else:
    print('small')

# java, c, c++, javascript (삼항 연산자)
# print(a > 5 ? 'big' : 'small')
print('big' if a > 5 else 'small')

# if ~ elif ~ else
n = 10
if n > 0:
    print('양수')
elif n < 0:
    print('음수')
else:
    print('0')

price = 0
order = 'nuddle'

if order == 'spam':
    price = 1000
elif order == 'egg':
    price = 200
elif order == 'spagetti':
    price = 2000

print('order: %s, price:%d' % (order, price))




