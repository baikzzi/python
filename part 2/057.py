try:
    print('안녕하세요.')
    print(param)
except:
    print('예외가 발생했습니다!')
finally: #오류 발생 유무와 상관없이 무조건 실행되는 코드
    print('무조건 실행하는 코드')