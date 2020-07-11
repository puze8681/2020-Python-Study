n = int(input('Enter an integer (2 or greater): '))
factor = 2
factors = []

while 1:
    if n%factor == 0:
        factors.append(factor)
        if n / factor == 1:
            for i in factors:
                print(i)
            break
        else:
            n = n / factor
    else:
        factor += 1