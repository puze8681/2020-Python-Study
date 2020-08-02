def sieve(limit):
    primeList = []
    for i in range(0, limit+1):
        primeList.append(i)
    del primeList[primeList.index(0)]
    del primeList[primeList.index(1)]
    p = 2
    while p < limit:
        i = 2
        while p*i < limit:
            if p*i in primeList:
                del primeList[primeList.index(p*i)]
            i += 1
        p = primeList[primeList.index(p) + 1]
    return primeList


print(sieve(int(input('limit 을 입력해주세요. '))))