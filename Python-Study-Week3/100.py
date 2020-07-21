def determine(year, month):
    if 1 <= month <= 12:
        if month == 2:
            if year % 400 == 0:
                print("29")
            elif year % 100 == 0:
                print("28")
            elif year % 4 == 0:
                print("29")
            else:
                print("28")
        else:
            print(str({1:31, 3:31, 4:30, 5:31, 6:30, 7:31,8:31, 9:30, 10:31, 11:30, 12:31}.get(month, 0)))
    else:
        print("정확히 입력해주세요.")


determine(int(input('년도를 입력하세요. ')), int(input('월을 입력하세요. ')))