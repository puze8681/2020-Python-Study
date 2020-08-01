def countRange(dList, min, max):
    count = 0
    for d in dList:
        if min <= d < max:
            count += 1
    return count


digitList = []
while 1:
    num = input('정수를 입력하세요. ')
    if num == "":
        break
    digitList.insert(0, float(num))
print(countRange(digitList, float(input('최소값을 입력하세요. ')), float(input('최대값을 입력하세요. '))))
