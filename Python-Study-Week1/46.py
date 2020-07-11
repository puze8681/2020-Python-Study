a = input('날짜를 입력하세요. ')
month = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}.get(a.split()[0], -1)
date = int(a.split()[1])

if 1 <= month <= 3:
    if month == 3 and date >= 20:
        print("Spring")
    else:
        print("Winter")
elif 4 <= month <= 6:
    if month == 6 and date >= 21:
        print("Summer")
    else:
        print("Spring")
elif 7 <= month <= 9:
    if month == 9 and date >= 22:
        print("Fall")
    else:
        print("Summer")
elif 10 <= month <= 12:
    if month == 12 and date >= 21:
        print("Winter")
    else:
        print("Fall")
else:
    print("Err")

