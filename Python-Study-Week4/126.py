def returnList(subList):
    subList.sort()
    resultList = [[]]
    for i in range(len(subList)):
        for j in range(i, len(subList)):
            tempList = []
            for k in range(i, j+1):
                tempList.append(subList[k])
            print(tempList)
            resultList.append(tempList)
    resultList.sort()
    print(resultList)


digitList = []
while 1:
    num = input('배열의 목록을 입력해주세요. ')
    if num == "":
        break
    digitList.append(int(num))
returnList(digitList)