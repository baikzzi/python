f = open('stockcode', 'r')
h = open('stockcode_copy.txt', 'w')

data = f.read()
h.write(data)

f.close()
h.close()
