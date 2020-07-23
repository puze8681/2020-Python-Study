digitList = []
while 1:
    num = input('정수를 입력하세요. ')
    if num == "":
        break
    num = int(num)
    digitList.append(num)
average = sum(digitList) / len(digitList)
for e in digitList:
    if e < average:
        print("평균 이하 값: {}".format(e))
    elif e > average:
        print("평균 이상 값: {}".format(e))
    else:
        print("평균 값: {}".format(e))