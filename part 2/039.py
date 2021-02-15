def add_number(n1, n2):
    ret = n1 +n2
    return ret

def add_txt(t1, t2):
    print(t1 + t2)

ans = add_number(10, 15)
print(ans) #add_number 함수에 10, 15를 넣어 더한 갚을 리턴받아 ans에 저장 후 출력 25
text1 = '대한민국~'
text2 = '만세!!'
add_txt(text1, text2) #add_txt함수에 text1과 text2를 넣으면 두 text가 더한 값이 출력된다.
