strdata = 'Time is money!!'
print(strdata[1:5]) #인덱스 1부터 4까지, 'ime '가 출력됨
print(strdata[:7]) #처음부터 인데스 6까지, 'Time is'가 출력됨
print(strdata[9:]) #인덱스 9부터 끝까지, 'oney!!'가 출력됨
print(strdata[:-3]) #처음부터 인덱스 -4까지, 'Time is mone'가 출력됨
print(strdata[-3:]) #인덱스 -3부터 끝까지, 'y!!'가 출력됨
print(strdata[:]) #처음부터 끝까지, 'Time is money!!'가 출력됨
print(strdata[::2]) #처음부터 끝까지 인덱스 2씩 더하며, 'Tm smny!'가 출력됨 