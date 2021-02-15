txt = 'A lot of things occur each day, every day.'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30) #인덱스 30 이후부터 문자 찾기
print(offset1) #22
print(offset2) #27
print(offset3) #38
#해당 문자의 첫 인덱스를 리턴
#문자열에서 문자를 못찾으면 -1 리턴