import random


def shuffleList(bingoList):
    # 카드 섞는 동작을 15번 진행함
    for i in range(0, 15):
        # 카드를 섞을 임의의 index 를 두개 만듬
        base = random.randint(0, 14)
        rebase = random.randint(0, 14)

        # 리스트의 두 원소의 위치를 바꿔주어 리스트를 섞음
        temp = bingoList[base]
        bingoList[base] = bingoList[rebase]
        bingoList[rebase] = temp

    # 반환해줄 resultList 에는 5개까지의 값만 추가해줌
    resultList = []
    for i in range(0, 5):
        resultList.append(bingoList[i])
    return resultList


def shuffleBingo():
    # 빙고게임 판에서 각 B, I, N, G, O 열에 해당하는 숫자를 넣을 리스트 생성
    listB = []
    listI = []
    listN = []
    listG = []
    listO = []

    for i in range(1, 76):
        if i < 16:
            # listB 에 해당되는 숫자인 1~15 추가
            listB.append(i)
        elif 16 <= i < 31:
            # listI 에 해당되는 숫자인 16~30 추가
            listI.append(i)
        elif 31 <= i < 46:
            # listN 에 해당되는 숫자인 31~45 추가
            listN.append(i)
        elif 46 <= i < 61:
            # listG 에 해당되는 숫자인 46~60 추가
            listG.append(i)
        else:
            # listO 에 해당되는 숫자인 61~75 추가
            listO.append(i)

    # 빙고게임 판에는 각 열마다 5개의 숫자가 표시되기 때문에 적절히 섞어 5개만 남겨진 리스트 만들어줌
    listB = shuffleList(listB)
    listI = shuffleList(listI)
    listN = shuffleList(listN)
    listG = shuffleList(listG)
    listO = shuffleList(listO)

    # 빙고 게임 판에 표시할 리스트들을 value 의 형태가 list 인 dictionary 형태로 반환함
    return {'B': listB, 'I': listI, 'N': listN, 'G': listG, 'O': listO}


def displayBingo(bingoDictionary):
    print("{:>3} {:>3} {:>3} {:>3} {:>3}".format("B", "I", "N", "G", "O"))
    # 각 dictionary 들의 value 인 리스트에서 반복문을 통해 5개의 값을 추출하여 빙고 게임 판에 출력
    for i in range(0, 5):
        print("{:>3} {:>3} {:>3} {:>3} {:>3}".format(bingoDictionary.get('B')[i], bingoDictionary.get('I')[i], bingoDictionary.get('N')[i], bingoDictionary.get('G')[i], bingoDictionary.get('O')[i]))


displayBingo(shuffleBingo())
