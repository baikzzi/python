x = 1
total = 0
while 1: #1은 True 이므로 무한 반복 break로 끝내줘야 함
    total += x
    if total > 100000:
        print(x)
        print(total)
        break
    x += 1
