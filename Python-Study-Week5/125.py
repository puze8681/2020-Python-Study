def isSubList(larger, smaller):
    if smaller in returnList(larger):
        return True
    else:
        return False


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
    return resultList


largerList = []
while 1:
    num = input('큰 배열의 목록을 입력해주세요. ')
    if num == "":
        break
    largerList.append(int(num))
smallerList = []
while 1:
    num = input('작은 배열의 목록을 입력해주세요. ')
    if num == "":
        break
    smallerList.append(int(num))
print(isSubList(largerList, smallerList))