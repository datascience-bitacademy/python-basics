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
f.close()

print('======= line 단위로 읽기1 =======')
linenum = 0
f1 = open('04.fileio2.py', 'rt', encoding='utf-8')
while True:
    line = f1.readline()
    if line == '':
        f1.close()
        break
    linenum += 1
    print(f'{linenum}:{line}', end='')

print('======= line 단위로 읽기2 =======')
f2 = open('04.fileio2.py', 'rt', encoding='utf-8')
lines = f2.readlines()
f2.close()
for linenum, line in enumerate(lines):
    print(f'{linenum+1}:{line}', end='')

print('======= with ~ as (자원정리를 자동으로 해준다) =======')
with open('04.fileio2.py', 'rt', encoding='utf-8') as f3:
    lines = f3.readlines()
    for linenum, line in enumerate(lines):
        print(f'{linenum+1}:{line}', end='')
