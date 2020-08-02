import decimal

# xy - 시그마 x * 시그마 y
# (시그마 x제곱 * n) - (시그마 x)제곱


def sigma(sigmaList):
    sum = 0
    for data in sigmaList:
        sum += data
    return sum


def sigma2(sigmaList1, sigmaList2):
    sum = 0
    for i in range(0, len(sigmaList1)):
        sum += (sigmaList1[i] * sigmaList2[i])
    return sum


def sigma3(sigmaList):
    sum = 0
    for data in sigmaList:
        sum += (data ** 2)
    return sum


def getList(dataList, index):
    returnList = []
    for data in dataList:
        returnList.append(data[index])
    return returnList


pointCount = 0
pointList = []
totalDistance = 0
while 1:
    if pointCount == 0:
        x = decimal.Decimal(input('Enter the x part of the coordinate: '))
        y = decimal.Decimal(input('Enter the y part of the coordinate: '))
        pointList.append((x, y))
        pointCount += 1
    else:
        x = input('Enter the x part of the coordinate: (blank to quit):')
        if x == "":
            n = len(pointList)
            xList = getList(pointList, 0)
            yList = getList(pointList, 1)
            sigmaX = sigma(xList)
            sigmaY = sigma(xList)
            sigmaXY = sigma2(xList, yList)
            sigmaX2 = sigma3(xList)

            m = (sigmaXY - ((sigmaX * sigmaY) / n)) / (sigmaX2 - ((sigmaX ** 2) / n))
            b = (sigmaY / n) - (m * (sigmaX / n))
            isEndWith0 = False
            while not isEndWith0:
                b = str(b)
                if '.' in b:
                    if b[len(b) - 1] == '.' or b[len(b)-1] == '0':
                        b = list(b)
                        del b[len(b) - 1]
                        b = ''.join(b)
                    else:
                        isEndWith0 = True
                else:
                    isEndWith0 = True
            b = decimal.Decimal(b)
            print("y = {}x + {}".format(m, b))
            break
        else:
            x = decimal.Decimal(x)
            y = decimal.Decimal(input('Enter the y part of the coordinate: '))
            pointList.append((x, y))
            pointCount += 1