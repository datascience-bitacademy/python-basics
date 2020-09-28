# 생성
l1 = []
l2 = [1, True, 'python', 3.14]


print("=============== sequence 타입 특징 ================")
# 인덱싱(sequence 타입 특징)
print(l2[0], l2[1], l2[2], l2[3]) # 정방향 인덱스
print(l2[-4], l2[-3], l2[-2], l2[-1]) # 역방향 인덱스

# slicing(sequence 타입 특징)
print(l2[1:4])
print(l2[:])    # 처음부터 끝까지
print(l2[2:]) # 2번 인덱스부터 끝까지
print(l2[len(l2)::-1])  # Step이 음수면 방향이 반대

# 반복(sequence 타입 특징)
l3 = l2 * 2
print(l3)

# 연결(sequence 타입 특징)
l4 = l2 + [1, 2, 3]
print(l4)

# 길이(sequence 타입 특징)
print(len(l4))

# in, not in(sequence 타입 특징)
print(5 not in l4)
print('python' in l4)

print("=============== 변경 가능한 객체 ================")
# 삭제(변경 가능한 객체)
del l4[2]
print(l4)

# 변경 가능한 객체(mutable)
l5 = ['apple', 'banana', 10, 20]
print(l5)
l5[2] = l5[2] + 90
print(l5)

print("=============== slicing 기법 ================")    # 중요
# 삭제(slicing을 이용한...)
l6 = [1, 12, 123, 1234]
l6[1:3] = [] # 슬라이싱 활용 삭제 기법
print(l6)

l6[0:] = []
print(l6)

# 삽입(slicing을 이용한...)
l7 = [1, 123, 1234, 12345]

# 중간 삽입
l7[1:1] = [12]
print(l7)

# 마지막 삽입
l7[5:] = [123456, 1234567]
print(l7)

# 처음 삽입
l7[:0] = [-123, -12, -1, 0]
print(l7)

# 치환(slicing을 이용한...)
l8 = [1, 12, 123, 1234, 12345]
print(l8)

l8[0:2] = [10, 20]
print(l8)

l8[0:2] = [100]
print(l8)

l8[1:2] = [200]
print(l8)

l8[2:4] = [300, 400, 500, 600]
print(l8)

print("=============== 객체함수 ================")
l9 = [1, 3, 4]

# 중간삽입
l9.insert(1, 2)
print(l9)

# 마지막 삽입
l9.append(5)
print(l9)

# 처음 삽입
l9.insert(0, 0)
print(l9)

# reverse
l9.reverse() # 객체의 메서드는 내부 데이터를 변경
print(l9)

l10 = reversed([1, 2, 3, 4, 5]) # -> 내부 데이터 변경 없이 순서가 반대인 제네레이터를 생성
print(l10);
# 파이썬의 제네레이터는 필요할 때 값을 생성해준다
print("l10의 요소 목록:", list(l10))

# 삭제(값으로 삭제 동질한 객체를 삭제한다. ==, 인덱스가 아닌 값의 삭제)
l9.remove(3)
print(l9)

# 없는 객체 삭제할 경우
try:
    l9.remove(3)
except ValueError as e:
    print('없는 객체 삭제할 경우 예외 발생')

# 확장 vs 연결(+) : 확장(extend)는 원본 리스트를 연장, 연결(+) 두 리스트가 합쳐진 새 리스트를 반환
l9.extend([-1, -2, -3, -4, -5])
print(l9)

# stack : append + pop
s = []
s.append(10)   # push
s.append(20)   # push
s.append(30)   # push
print(s)
print(s.pop())  # pop
print(s.pop())  # pop

print(s)

# queue로 사용해보기  : append + pop(0)
q = [1, 2]
q.append(3)
q.append(4)
q.append(5)
print(q)

print(q.pop(0))   # 1
print(q.pop(0))   # 2
print(q.pop(0))   # 3
print(q)

# sort : 리스트 내부 데이터를 변경
l10 = [1, 5, 3, 9, 8, 11]
l10.sort()  # 내부 객체를 변경하는 오름차순 정렬
print(l10)

l11 = [10, 2, 33, 9, 8, 4, 11]
# 키함수: 정렬 기준을 마련하는 함수
l11.sort(key=str)
print(l11)

l11.sort(key=int)
print(l11)

# cf: sorted 전역함수 : 내부 데이터 변경 없이 정렬 후 새 객체 반환
l12 = [19, 46, 37, 28, 91, 55, 64]
l13 = sorted(l12)
print(l13)


def f(i):
    return i % 10


l14 = sorted(l12, key=f, reverse=False)
print(l14)

# 순차 자료형의 경우 간단한 통계 함수를 사용할 수 있다
scores = [80, 90, 70, 100, 80, 90]
print("점수:", scores)
print("최저 점수:", min(scores))
print("최고 점수:", max(scores))
print("총점:", sum(scores))
print("평균:", sum(scores) / len(scores))