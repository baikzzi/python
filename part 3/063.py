a = 11113
b = 23
ret1, ret2 = divmod(a, b) #divmod는 (몫, 나머지)와 같이 듀플로 리턴
print('<%d/%d>는 몫이 <%d>, 나머지가 <%d> 입니다.'%(a, b, ret1, ret2))
