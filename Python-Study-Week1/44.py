a = input('날짜를 입력하세요. ')
month = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}.get(a.split()[0], -1)
date = int(a.split()[1])

if month == 1 and date == 1:
    print("New year's day")

elif month == 7 and date == 1:
    print("Canada")

elif month == 12 and date == 25:
    print("Christmas day")
else:
    print("No Holiday")

