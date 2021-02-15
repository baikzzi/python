txt = 'abcdefghijk'
ret = txt[::-1]
print(ret) #'kjihgfedcba'가 출력됨

ret1 = txt[::-2]
print(ret1) #거꾸로 된 순서로 홀수 번째 문자만 추출
ret2 = txt[-2::-2]
print(ret2) #거꾸로 된 순서로 짝수 번째 문자만 추출