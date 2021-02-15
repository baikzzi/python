spos = 105 #파일을 읽는 위치 지정
size = 500 #읽을 크기 지정

f = open('stockcode.txt', 'r')
h = open('stockcode_copy.txt', 'w')

f.seek(spos)
data = f.read(size)
h.write(data)

f.close()
h.close()
