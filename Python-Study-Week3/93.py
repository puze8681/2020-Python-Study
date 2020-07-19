def nextPrime(number):
    while 1:
        isPrime = True
        number += 1
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
        if isPrime:
            print("nextPrime is {}".format(number))
            break


nextPrime(int(input('숫자를 입력하세요. ')))
