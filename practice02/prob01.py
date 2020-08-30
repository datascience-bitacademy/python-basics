# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
s = '/usr/local/bin/python'

lst = s[1:].split('/')
r = ','.join(lst)
print(r)

# 디렉토리 경로명과 파일명을 분리하여 출력하세요.
r = ','.join(s.rsplit('/', 1))
print(r)