def perfect(nn):
    divisorList = []
    for d in range(1, nn):
        if nn % d == 0:
            divisorList.append(d)
    if sum(divisorList) == nn:
        print(nn)


for i in range(1, 10001):
    perfect(i)