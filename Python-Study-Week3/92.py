def prime(number):
    isPrime = True
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
        print(isPrime)
    else:
        print("1보다 큰 수를 입력해주세요.")


prime(int(input('숫자를 입력하세요. ')))
