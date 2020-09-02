
# text mode 가 default : t(생략가능)
f = open('test_t.txt', 'wt', encoding='utf-8')
w_sz = f.write('안녕하세요.\n파이썬입니다.')
f.close()
print(w_sz)

# binary mode : b
f = open('test_b.txt', 'wb')
w_sz = f.write(bytes('안녕하세요.\n파이썬입니다.', 'utf-8'))
f.close()
print(w_sz)

# read test : text mode
f = open('test_t.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)

# read test : binary mode -> copy.py


