import random
totalFlipCount = 0
for i in range(10):
    flipList = []
    flipCount = 0
    sameFlipCount = 0
    while 1:
        flip = {0: 'H', 1: 'T'}.get(random.randrange(0, 2))
        flipList.append(flip)
        if flipCount > 0:
            if flip == flipList[flipCount-1]:
                sameFlipCount += 1
            else:
                sameFlipCount = 0
        flipCount += 1
        if sameFlipCount == 2:
            for j in flipList:
                print(j, end=" ")
            print("({}".format(flipCount), "flips)")
            totalFlipCount += flipCount
            break
print("On average,",totalFlipCount/10, "flips were needed")