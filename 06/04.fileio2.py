f = open('test_t.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('---' + text + '----')

# position 단위는 byte
pos = f.tell()
print(pos)

# 1st Parameter: offset
# 2nd Parameter: (0: 파일의 처음, 1: 현재위치, 2:파일의 끝
f.seek(16, 0)
text = f.read()
print(text)

# line 단위로 읽기
open('fileio2.py', 'rt', encoding='utf-8')
