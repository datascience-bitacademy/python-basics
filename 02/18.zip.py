# zip() 사용 예
# 여러 순차형을 하나로 묶어준다

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three', 'four']

z = zip(seq1, seq2)
print(z, type(z))
for t in z:
    print(t)

# zip 객체는 한번 순회하면 내용이 비어버린다
# 제네레이터이므로 실제 내부 데이터는 담고 있지 않다
z = zip(seq1, seq2)
for index, t in enumerate(z):
    print(index, t)

z = zip(seq1, seq2)
for a, b in z:
    print(a, b)
