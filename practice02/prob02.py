# 다음과 같은 테스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
            To connect to the most powerful tolls int the world.
        </p>
    </body>
</html>"""

indexbegin = 0
while True:
    indexbegin = s.find('<', indexbegin)
    if indexbegin == -1:
        break
    indexend = s.find('>')
    if indexend != -1:
        s = s[:indexbegin] + s[indexend + 1:]
    else:
        indexend += 1

print(s)

