def formattingList(strList):
    result = ""
    for i in range(0, len(strList)):
        str = strList[i]
        if i != 0 and i == len(strList) -1:
            result += " and " + str
        elif i < len(strList) -2:
            result += str + ", "
        else:
            result += str
    print(result)


stringList = []
while 1:
    string = (input('정수를 입력하세요. '))
    if string == "":
        break
    stringList.append(string)
formattingList(stringList)