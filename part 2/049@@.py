class MyClass:
    var = '안녕하세요'
    def sayHello(self): #클래스 함수 선언시 들어가는 self에 대해서 물어보기
        print(self.var)

obj = MyClass() #MyClass 인스턴스 객체 생성
print(obj.var) #'안녕하세요'가 출력됨
obj.sayHello() #'안녕하세요'가 출력됨
