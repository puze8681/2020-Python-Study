import random


def shuffleList(bingoList):
    for i in range(0, 15):
        base = random.randint(0, 14)
        rebase = random.randint(0, 14)
        temp = bingoList[base]
        bingoList[base] = bingoList[rebase]
        bingoList[rebase] = temp
    resultList = []
    for i in range(0, 5):
        resultList.append(bingoList[i])
    return resultList


def shuffleBingo():
    listB = []
    listI = []
    listN = []
    listG = []
    listO = []

    for i in range(1, 76):
        if i < 16:
            listB.append(i)
        elif 16 <= i < 31:
            listI.append(i)
        elif 31 <= i < 46:
            listN.append(i)
        elif 46 <= i < 61:
            listG.append(i)
        else:
            listO.append(i)
    listB = shuffleList(listB)
    listI = shuffleList(listI)
    listN = shuffleList(listN)
    listG = shuffleList(listG)
    listO = shuffleList(listO)
    return {'B': listB, 'I': listI, 'N': listN, 'G': listG, 'O': listO}


def displayBingo(bingoDictionary):
    print("{:>3} {:>3} {:>3} {:>3} {:>3}".format("B", "I", "N", "G", "O"))
    for i in range(0, 5):
        print("{:>3} {:>3} {:>3} {:>3} {:>3}".format(bingoDictionary.get('B')[i], bingoDictionary.get('I')[i], bingoDictionary.get('N')[i], bingoDictionary.get('G')[i], bingoDictionary.get('O')[i]))


displayBingo(shuffleBingo())
