total = 0
while 1:
    price = input('가격을 입력해주세요. ')
    if price == "":
        print("입력된 모든 항목의 총 비용 :", total)
        print("현금으로 결제할 경우 지불해야 하는 금액:", int(round(total / 5, 0)))
        break;
    else:
        total += int(price)
