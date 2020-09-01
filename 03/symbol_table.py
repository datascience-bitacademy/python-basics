# global, local 심벌테이블 확인
g_a = 1
g_s = '마이콜'


def g_f():
    l_a = 2
    l_s = '둘리'
    a = 2
    print(locals())


print('====== Global Symbol Table VS Local Symbol Table ======')
print(globals())
g_f()

print(g_a)
# error: local symbol table은 함수가 실행이 끝나면 사라진다.
# print(l_a)

print('====== Object Symbol Table ======')

g_f.n = 'hello'
g_f.i = 10
print(g_f.__dict__)




