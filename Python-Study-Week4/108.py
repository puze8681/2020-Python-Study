digitList = []
while 1:
    num = input('정수를 입력하세요. ')
    if num == "":
        break
    num = int(num)
    digitList.append(num)
negativeList = []
zeroList = []
positiveList = []
for d in digitList:
    if d < 0:
        negativeList.append(d)
    elif d > 0:
        positiveList.append(d)
    else:
        zeroList.append(d)
resultList = negativeList + zeroList + positiveList
print(resultList)
