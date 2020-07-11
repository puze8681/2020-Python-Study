total = 0
while 1:
    age = input("나이를 입력하세요. ")
    if age == "":
        print("전체 입장료 :", format(total, ".2f"))
        break
    else:
        age = int(age)
        if 0 <= age <= 2:
            total+=0
        elif 3 <= age <= 12:
            total += 14
        elif age >= 65:
            total += 18
        else:
            total += 23