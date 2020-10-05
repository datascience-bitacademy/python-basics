def handling_exception():
    lst = []
    try:
        print("예외 가능 코드 블록")

        if len(lst) > 3: # 방어 코드
            lst[3] = 1

        # result = 4 / 0
        if "String".isdigit():
            int("String")
    except IndexError as e: # 구체적 예외
        print(e, type(e))
    except ZeroDivisionError as e:
        print(e, type(e))
    except ValueError as e:
        print(e, type(e))
    except Exception as e: # 처리되지 않은 모든 예외
        print(e, type(e))
    else: # 예외가 없을 때(모두 정상 처리)
        print("예외 없이 코드를 수행하였습니다.")
    finally: # 예외 유무 상관 없이 항상 마지막에 수행 -> 자원의 정리작업
        print("예외 처리 종료")

    # 예외가 있을 시: try -> except -> finally
    # 예외 없을시 : try -> else -> finally

    print("End of Code")


def caller(): # 호출하는 함수
    try:
        result = callee(4, 0)
    except ZeroDivisionError as e:
        print(e, type(e))
    else:
        print(result)


def callee(a, b): # 호출되는 함수
    """
    호출 되는 함수는 내부에서 완벽하게 예외를 처리해 복구하기 힘들다면
    홀출 한 함수로 예외처리를 위임하는 것이 더 좋다
    raise  예외객체
    """
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없어요")

    return str.format("{} / {} = {}".format(a, b, a / b))

if __name__ == "__main__":
    # handling_exception()
    caller()
