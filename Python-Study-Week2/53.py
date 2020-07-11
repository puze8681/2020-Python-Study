rating = float(input('종업원의 등급을 입력하세요. '))
if rating == 0.0:
    print("Unacceptable performance")
elif rating == 0.4:
    print("Acceptable performance")
    print("raise :", 2400.00 * 0.4)
elif rating >= 0.6:
    print("Meritorious performance")
    print("raise :", 2400.00 * rating)
else:
    print("잘못된 입력입니다.")