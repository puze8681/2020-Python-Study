def analysing(paramList, n):
    if len(paramList) < n * 2:
        return print("리스트의 원소 개수가 너무 적습니다.")

    paramList.sort()
    resultList = []
    for i in range(n, len(paramList)-n):
        resultList.append(paramList[i])
    print(resultList)


digitList = []
while 1:
    num = int(input('정수를 입력하세요. '))
    if num == 0:
        break
    digitList.append(num)
analysing(digitList, int(input('제거할 원소 개수를 입력하세요. ')))