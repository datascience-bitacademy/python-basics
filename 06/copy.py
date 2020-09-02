import sys

args = sys.argv[1:]

try:
    f_src = open(args[0], 'rb')
    data = f_src.read()
    f_src.close()

    f_dst = open(args[1], 'wb')
    f_dst.write(data)
    f_dst.close()
except FileNotFoundError as e:
    print('파일이 존재하지 않습니다:' + str(e))


