import datetime


def get_datetime():
    # 현재 시간
    now = datetime.datetime.now()
    print("현재 시간:", now)

    # 생성자 활용
    dt = datetime.datetime(1999, 12, 31)    # 최소 연월일인 지정
    print(dt)

    # 속성들
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
    print(dt, "는 무슨 요일?", dt.weekday()) # 0 -> 월

    # 날짜 객체의 반환
    print(now.date(), type(now.date()))
    # 시간 객체의 반환
    print(now.time(), type(now.time()))


def timedelta_ex():
    # 두 datetime은 대소를 비교할 수 있고
    # 두 datetime의 차이를 얻을 수 있다 -> timedelta
    now = datetime.datetime.now() # 현재
    past = datetime.datetime(1999, 12, 31) # 과거

    print(now > past)

    diff = now - past # 두 datetime의 차이
    print(diff, type(diff)) # timedelta

    # datetime과 timedelta의 합산 -> 새로운 날짜
    # 오늘로부터 100일 후가 무슨 날인가?
    future = now + datetime.timedelta(days=100)
    print("100일 후:", future)


def format_date():
    # datetime -> str : strftime
    # str -> datetime : strptime
    now = datetime.datetime.now()

    print("strftime:", now.strftime("%Y-%m-%d %H-%M-%S"))

    s = "1999-12-31 23:59"
    dt = datetime.datetime.strptime(s,  # 문자열
                                    "%Y-%m-%d %H:%M")   # 날짜 포맷
    print("strptime:", dt, type(dt))


if __name__ == "__main__":
    # get_datetime()
    # timedelta_ex()
    format_date()