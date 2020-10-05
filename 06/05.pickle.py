# pickle 모듈
# 객체를 직렬화, 역직렬화 하는 모듈

import pickle

def test_pickle_dump():
    # 직렬화 예제
    with open("thieves.bin", "wb") as f: # 파일모드는 반드시 binary여야 한다
        try:
            pickle.dump({"name": "홍길동", "age": 25}, f)
        except Exception as e:
            print(e, type(e))
            print("데이터를 덤프하지 못했습니다.")
        else:
            print("데이터를 덤프했습니다.")


def test_pickle_load():
    # 역직렬화 예제
    with open("thieves.bin", "rb") as f:
        try:
            thief = pickle.load(f)
        except Exception as e:
            print(e, type(e))
            print("데이터를 로드하지 못했습니다.")
        else:
            print("데이터를 로드했습니다.")
            print(thief, type(thief))


def test_pickle_multi_dump():
    # 한 파일에 여러 객체를 직렬화하려면
    # dump 중복 수행
    t1 = { "name": "홍길동", "age": 25 }
    t2 = { "name": "장길산", "age": 40 }
    t3 = { "name": "임꺽정", "age": 35 }

    with open("thieves.bin", "wb") as f:
        try:
            pickle.dump(t1, f)
            pickle.dump(t2, f)
            pickle.dump(t3, f)
        except Exception as e:
            print(e, type(e))
        else:
            print("데이터를 덤프했습니다.")


def test_pickle_multi_load():
    # thieves.bin에서 사전을 역직렬화 하여 리스트에 담아 봅시다
    thieves = []
    with open("thieves.bin", "rb") as f:
        """
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))
        print(pickle.load(f))   # EOFError
        """
        while True:
            try:
                thief = pickle.load(f) # 역직렬화
                thieves.append(thief)
            except EOFError as e:
                # 더 이상 읽어들일 pickle이 없다
                break

        print(thieves)


if __name__ == "__main__":
    # test_pickle_dump()
    # test_pickle_load()
    # test_pickle_multi_dump()
    test_pickle_multi_load()