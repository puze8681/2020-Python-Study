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
    # 화면을 계속 다시 그리기 위해 그렸던 화면을 지워줌
    os.system('clear')
    print("{:>19}".format("call count: {}").format(len(bingoList)))
    print("{:>3} {:>3} {:>3} {:>3} {:>3}".format("B", "I", "N", "G", "O"))

    # 각각 horizontal 빙고를 뜻하는 key 값 (0,1,2,3,4) 와
    # vertical 빙고를 뜻하는 key 값 (B,I,N,G,O) 와
    # diagonal 빙고를 뜻하는 key 값 (LU, RU) 들에 각각 빙고판과 빙고숫자의 겹친 개수를 value 로 하는 dictionary 생성
    # LU 는 LightUp, RU 는 RightUp 의 약자로 대각선의 시작 방향을 뜻함
    count = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, 'B': 0, 'I': 0, 'N': 0, 'G': 0, 'O': 0, 'LU': 0, 'RU': 0,}
    for i in range(0, 5):
        indexB = bingoDictionary.get('B')[i]
        indexI = bingoDictionary.get('I')[i]
        indexN = bingoDictionary.get('N')[i]
        indexG = bingoDictionary.get('G')[i]
        indexO = bingoDictionary.get('O')[i]
        # indexB 의 값이 빙고숫자와 겹치면
        if indexB in bingoList:
            # horizontal i 와 vertical B 의 count 를 증가시킴
            count[str(i)] += 1
            count['B'] += 1

            # i 가 0 이라면 diagonal LU (왼쪽 대각선) 의 count 를 증가시킴
            if i == 0:
                count['LU'] += 1

            # i 가 4 이라면 diagonal RU (오른쪽 대각선) 의 count 를 증가시킴
            if i == 4:
                count['RU'] += 1

            # 출력될 글자에 색을 입혀 출력
            print("\033[95m{:>3} \033[0m".format(indexB), end="")
        else:
            print("{:>3} ".format(indexB), end="")

        # indexI 의 값이 빙고숫자와 겹치면
        if indexI in bingoList:
            # horizontal i 와 vertical I 의 count 를 증가시킴
            count[str(i)] += 1
            count['I'] += 1

            # i 가 1 이라면 diagonal LU (왼쪽 대각선) 의 count 를 증가시킴
            if i == 1:
                count['LU'] += 1

            # i 가 3 이라면 diagonal RU (오른쪽 대각선) 의 count 를 증가시킴
            if i == 3:
                count['RU'] += 1

            # 출력될 글자에 색을 입혀 출력
            print("\033[95m{:>3} \033[0m".format(indexI), end="")
        else:
            print("{:>3} ".format(indexI), end="")

        # indexN 의 값이 빙고숫자와 겹치면
        if indexN in bingoList:
            # horizontal i 와 vertical N 의 count 를 증가시킴
            count[str(i)] += 1
            count['N'] += 1

            # i 가 2 이라면 diagonal LU (왼쪽 대각선) 와 RU (오른쪽 대각선) 의 count 를 증가시킴
            if i == 2:
                count['LU'] += 1
                count['RU'] += 1

            # 출력될 글자에 색을 입혀 출력
            print("\033[95m{:>3} \033[0m".format(indexN), end="")
        else:
            print("{:>3} ".format(indexN), end="")

        # indexG 의 값이 빙고숫자와 겹치면
        if indexG in bingoList:
            # horizontal i 와 vertical G 의 count 를 증가시킴
            count[str(i)] += 1
            count['G'] += 1

            # i 가 3 이라면 diagonal LU (왼쪽 대각선) 의 count 를 증가시킴
            if i == 3:
                count['LU'] += 1

            # i 가 1 이라면 diagonal RU (오른쪽 대각선) 의 count 를 증가시킴
            if i == 1:
                count['RU'] += 1

            # 출력될 글자에 색을 입혀 출력
            print("\033[95m{:>3} \033[0m".format(indexG), end="")
        else:
            print("{:>3} ".format(indexG), end="")

        # indexO 의 값이 빙고숫자와 겹치면
        if indexO in bingoList:
            # horizontal i 와 vertical O 의 count 를 증가시킴
            count[str(i)] += 1
            count['O'] += 1

            # i 가 4 이라면 diagonal LU (왼쪽 대각선) 의 count 를 증가시킴
            if i == 4:
                count['LU'] += 1

            # i 가 0 이라면 diagonal RU (오른쪽 대각선) 의 count 를 증가시킴
            if i == 0:
                count['RU'] += 1

            # 출력될 글자에 색을 입혀 출력
            print("\033[95m{:>3}\033[0m".format(indexO))
        else:
            print("{:>3}".format(indexO))

    # 빙고 숫자 리스트를 정렬하여 출력 시 겹치는 숫자 없이 생성이 옳게 되었는지 확인
    bingoList.sort()
    print("\nbingoList: {}".format(bingoList))

    # count 라는 dictionary 의 value 중 5인 것이 있다면 빙고임을 확인, False 반환
    # 그렇지 않다면 True 반환하여 빙고게임을 계속 진행함
    for key, value in count.items():
        if value == 5:
            print("\nBINGO !!!")
            return False
    return True


def bingoPlay():
    # 섞은 빙고판을 shuffleDeck에 선언
    shuffleDeck = shuffleBingo()
    # 빙고게임이 끝났는지(빙고 완성) 여부를 파악하는 isPlaying 변수 선언
    isPlaying = True
    # 1~75 까지의 임의의 값을 넣을 bingo 리스트 선언
    bingo = []

    # 빙고가 완성되기 전까지 빙고 숫자를 계속 부름
    while isPlaying:
        # 빙고 게임판을 화면에 매끄럽게 그리기 위해 0.5초를 기준으로 실행시킴
        time.sleep(0.5)
        # 빙고 숫자를 부를 때 기존에 불렀던 값인지 파악하는 isOverlap 변수 선언
        isOverlap = True
        # 중복되지 않은 숫자를 부를 때 까지 임의의 숫자를 계속 재생성함
        while isOverlap:
            bingoElement = random.randint(1, 75)
            if bingoElement not in bingo:
                # 중복되지 않은 숫자를 부르면 bingo 리스트에 추가 후 isOverlap 변수를 False 로 변경하여 loop 탈출
                bingo.append(bingoElement)
                isOverlap = False

        # 빙고 판을 뜻하는 shuffleDeck 과 부른 빙고 숫자를 뜻하는 bingo 리스트를 파라미터로 하는 disPlayBingo 함수를 실행
        # 함수의 결과 값은 빙고 완성 여부임으로 빙고가 완성되었으면 False 를 반환하여 loop 탈출
        isPlaying = displayBingo(shuffleDeck, bingo)


bingoPlay()