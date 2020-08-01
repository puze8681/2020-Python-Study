strList = input('문자열을 입력하세요. ').split(" ")
for i in range(0, len(strList)):
    str = strList[i]
    for c in str:
        if not c.isalpha() and c != "'":
            strList[i] = str.replace(c, "")
print(strList)