a = int(input('인간 년도를 입력하세요. '))
if a < 0:
    print("음수를 입력하지 마세요.")
elif 0 <= a <= 2:
    print(a * 10.5)
else:
    print(a * 7 + 7)

