tuple1 = (1,2,3,4,5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1,2,3,4,5], ['a', 'b', 'c'])
#tuple1[0] = 6 #튜플은 리스트와 비슷한 성질을 갖고 있지만 요소의 값을 변경할 수 없다.

def myfunc():
    print('안녕하세요')

tuple4 = (1,2, myfunc)
tuple4[2]() #'안녕하세요'가 출력됨