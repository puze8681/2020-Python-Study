import random
import time
import os


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


def displayBingo(bingoDictionary, bingoList):
    # Windows 환경에서는 os.system('cls')
    os.system('clear')
    print("{:>19}".format("call count: {}").format(len(bingoList)))
    print("{:>3} {:>3} {:>3} {:>3} {:>3}".format("B", "I", "N", "G", "O"))
    count = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 'B': 0, 'I': 0, 'N': 0, 'G': 0, 'O': 0, 'L': 0, 'R': 0,}
    for i in range(0, 5):
        indexB = bingoDictionary.get('B')[i]
        indexI = bingoDictionary.get('I')[i]
        indexN = bingoDictionary.get('N')[i]
        indexG = bingoDictionary.get('G')[i]
        indexO = bingoDictionary.get('O')[i]
        if indexB in bingoList:
            count[str(i)] += 1
            count['B'] += 1
            print("\033[95m{:>3} \033[0m".format(indexB), end="")
        else:
            print("{:>3} ".format(indexB), end="")
        if indexI in bingoList:
            count[str(i)] += 1
            count['I'] += 1
            print("\033[95m{:>3} \033[0m".format(indexI), end="")
        else:
            print("{:>3} ".format(indexI), end="")
        if indexN in bingoList:
            count[str(i)] += 1
            count['N'] += 1
            print("\033[95m{:>3} \033[0m".format(indexN), end="")
        else:
            print("{:>3} ".format(indexN), end="")
        if indexG in bingoList:
            count[str(i)] += 1
            count['G'] += 1
            print("\033[95m{:>3} \033[0m".format(indexG), end="")
        else:
            print("{:>3} ".format(indexG), end="")
        if indexO in bingoList:
            count[str(i)] += 1
            count['O'] += 1
            print("\033[95m{:>3}\033[0m".format(indexO))
        else:
            print("{:>3}".format(indexO))
    bingoList.sort()
    print("\nbingoList: {}".format(bingoList))
    for key, value in count.items():
        if value == 5:
            print("\nBINGO !!!")
            return False
    return True


def bingoPlay():
    shuffleDeck = shuffleBingo()
    isPlaying = True
    bingo = []
    while isPlaying:
        time.sleep(0.5)
        isOverlap = True
        while isOverlap:
            bingoElement = random.randint(1, 75)
            if bingoElement not in bingo:
                bingo.append(bingoElement)
                isOverlap = False
        isPlaying = displayBingo(shuffleDeck, bingo)
        if not isPlaying:
            return len(bingo)


bingoPlay()