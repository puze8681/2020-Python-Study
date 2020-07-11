a = input('날짜를 입력하세요. ')
month = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}.get(a.split()[0], -1)
date = int(a.split()[1])

if month == 1:
    if date <= 19:
        print("Capricorn")
    else:
        print("Aquarius")
elif month == 2:
    if date <= 18:
        print("Aquarius")
    else:
        print("Pisces")
elif month == 3:
    if date <= 20:
        print("Pisces")
    else:
        print("Aries")
elif month == 4:
    if date <= 19:
        print("Aries")
    else:
        print("Taurus")
elif month == 5:
    if date <= 20:
        print("Taurus")
    else:
        print("Gemini")
elif month == 6:
    if date <= 20:
        print("Gemini")
    else:
        print("Cancer")
elif month == 7:
    if date <= 22:
        print("Cancer")
    else:
        print("Leo")
elif month == 8:
    if date <= 22:
        print("Leo")
    else:
        print("Virgo")
elif month == 9:
    if date <= 22:
        print("Virgo")
    else:
        print("Libra")
elif month == 10:
    if date <= 22:
        print("Libra")
    else:
        print("Scorpio")
elif month == 11:
    if date <= 21:
        print("Scorpio")
    else:
        print("Sagittarius")
elif month == 12:
    if date <= 21:
        print("Sagittarius")
    else:
        print("Capricorn")
else:
    print("ERR")