a = list(input('위치를 입력하세요. '))

if (ord(a[0]) + int(a[1])) % 2 == 0:
    print("정사각형이 검은색입니다.")
else:
    print("정사각형이 하얀색입니다.")

