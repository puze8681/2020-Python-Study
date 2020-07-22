digitList = []
while 1:
    num = int(input('정수를 입력하세요. '))
    if num == 0:
        break
    digitList.append(num)
digitList.sort()
print(digitList)