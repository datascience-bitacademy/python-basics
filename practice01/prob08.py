# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.


def reverse(s):
    r = ''
    for i in range(1, len(s)+1):
        r += s[len(s)-i]
    return r
#   return s[::-1]


instr = input('입력> ')
print('결과> ' + reverse(instr))
