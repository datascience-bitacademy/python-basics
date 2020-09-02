def f(x):
    r = x * x
    return r


for i in range(10):
    s = '{0}:{1}'.format(i, (lambda x: x * x)(i))
    print(s)

