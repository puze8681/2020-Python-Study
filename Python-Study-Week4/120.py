print("빈칸 입력 시 입력 종료입니다.")
valueList = []

while 1:
    num = input('배열의 목록을 입력해주세요. ')
    if num == "":
        break
    valueList.append(int(num))
if len(valueList) == 0:
    print("목록이 비어있습니다.")
elif len(valueList) == 1:
    print("목록이 한칸밖에 없습니다.")
else:
    isSorted = True
    isReSorted = True
    sortedList = valueList[:]
    sortedList.sort()
    for i in range(len(valueList)):
        if valueList[i] != sortedList[i]:
            isSorted = False
        elif valueList[i] != sortedList[len(valueList)-i-1]:
            isReSorted = False

    if isSorted:
        print("목록이 오름차순으로 정렬되어 있습니다.")
    elif isReSorted:
        print("목록이 내림차순으로 정렬되어 있습니다.")
    else:
        print("목록이 정렬되어 있지 않습니다.")

