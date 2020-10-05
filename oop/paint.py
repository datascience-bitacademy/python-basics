from oop.point import Point, ColorPoint


def test_bound_instance_method():
    # 객체 인스턴스를 직접 호출하여 접근하는 방법
    # 인수로 self는 전달하지 않음
    p = Point()
    p.set_x(10)
    p.set_y(20)
    p.draw()


def test_unbound_class_method():
    # 클래스 객체를 통해 우회 접근
    # self 인수에 객체의 참조 주소를 전달 해야 함
    p = Point()
    Point.set_x(p, 10)
    Point.set_y(p, 20)
    Point.draw(p)


def test_other_methods():
    # static, class 멤버에 접근
    print("참조 카운트:", Point.get_count_of_instance())
    Point.static_method()


def test_constructor():
    p1 = Point(10, 20)  # __init__ 수행
    print("x={}, y={}, count_of_instance={}".format(p1.x, p1.y, Point.get_count_of_instance()))
    p2 = Point(100, 200)
    print("x={}, y={}, count_of_instance={}".format(p2.x, p2.y, Point.get_count_of_instance()))

    del p1 # __del__ 소멸자 수행
    print("count_of_instance = {}".format(Point.get_count_of_instance()))


def test_to_string():
    p = Point(10, 20)
    print("p = ", p)

    # repr 함수 -> __repr__ 메서드가 수행
    print("repr(p)", repr(p))

    p2 = eval(repr(p)) # repr을 이용한 객체의 복원
    print(p2, type(p2))


def test_operator():
    p = Point(10, 20)
    print("p + int:", p + 10)

    print("Point + Point:", p + Point(10, 20))  # __add__ 호출

    print("Point - Point:", p - Point(10, 10)) # __sub__ 호출

    print("Point == Point:", p == Point(10, 20)) # __eq__ 호출

    print("int + Point:", 10 + p) # Point.__radd__ 호출



def test_inheritance(): # 상속 테스트
    cp = ColorPoint(10, 20, "red")
    print("cp:", cp)
    cp.draw()

    print(dir(cp))  # 내부 멤버 확인


if __name__ == "__main__":
    # test_bound_instance_method()
    # test_unbound_class_method()
    # test_other_methods()
    # test_constructor()
    # test_to_string()
    # test_operator()
    test_inheritance()