names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
ks = names.keys()
print(ks)

for k in ks:
    print('Key:%s\tValue:%d'%(k, names[k]))

#딕셔너리 names의 키를 받아 리스트 ks로 만들었다.
#for문에 ks를 넣어 순서대로 Key:에 출력, names[]에 넣어 그에 맞는 값도 같이 출력