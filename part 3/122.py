listdata1 = [0,1,2,3,4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]
print(all(listdata1)) #False
print(any(listdata1)) #True
print(all(listdata2)) #True
print(any(listdata2)) #True
print(all(listdata3)) #False
print(any(listdata3)) #False