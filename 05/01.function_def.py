def dummy():
    pass


def my_function():
    print('Hello World')


# 여러개 값을 반환할 수 있다.(사실은 tuple의 auto packing과 unpacking을 파이썬이 지원을 해준다.)
def my_function2():
    return 10, 20


def my_function3(id):
    print('{0}님 안녕하세요'.format(id))


def my_function4(a, b):
    return a * b


def none():
    print('some codes...1')
    if 10 - 9 is 1:
        return
    print('some codes...2')


# 함수는 객체다. (함수를 값 처럼 다룰 수 있다.)
def my_function5(f):
    f()


dummy()
my_function()

# t = my_function2()
# print(t)
i, j = my_function2()
print(i, j)

my_function3('kickscar')

r = my_function4(10, 20)
print(r)


my_function5(my_function)
print(my_function, type(my_function))