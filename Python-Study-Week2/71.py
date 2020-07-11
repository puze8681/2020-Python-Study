num = int(input('숫자를 입력하세요. '))
guess = num / 2
while 1:
    if abs(num - (guess * guess)) <= 10 ** -12:
        print(guess)
        break
    else:
        guess = (guess + (num/guess)) / 2