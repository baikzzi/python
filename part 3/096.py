u_txt = 'I love python'
b_txt = u_txt.encode() #문자열을 바이트 객체로 바꾸기
print(u_txt)
print(b_txt)

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1) #Ture
print(ret2) #False