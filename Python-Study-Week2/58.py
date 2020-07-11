year = int(input('년도를 입력하세요. '))
month = int(input('월을 입력하세요. '))
date = int(input('일을 입력하세요. '))

leap = False
if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False

if month < 1 or month > 12:
    print("월은 1~12 월까지 있습니다.")
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if date < 1 or date > 31:
        print("일은 1일부터 31일까지 있습니다.")
    elif date == 31:
        month += 1
        date = 1
        print(year, month, date)
    else:
        date += 1
        print(year, month, date)
elif month == 2:
    if leap:
        if date < 1 or date > 29:
            print("일은 1일부터 29일가지 있습니다.")
        elif date == 29:
            month += 1
            date = 1
            print(year, month, date)
        else:
            date += 1
            print(year, month, date)
    else:
        if date < 1 or date > 28:
            print("일은 1일부터 28일까지 있습니다.")
        elif date == 28:
            month += 1
            date = 1
            print(year, month, date)
        else:
            date += 1
            print(year, month, date)
elif month == 12:
    if date < 1 or date > 31:
        print("일은 1일부터 31일까지 있습니다.")
    elif date == 31:
        year += 1
        month = 1
        date = 1
        print(year, month, date)
    else:
        date += 1
        print(year, month, date)
else:
    if date < 1 or date > 30:
        print("일은 1일부터 30일까지 있습니다.")
    elif date == 30:
        month += 1
        date = 1
        print(year, month, date)
    else:
        date += 1
        print(year, month, date)