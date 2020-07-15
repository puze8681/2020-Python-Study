import random
num = random.randrange(0,38)
if num == 0:
    print("The spin resulted in 0 ...\n")
    print("Pay 0")
elif num == 37:
    print("The spin resulted in 00 ...\n")
    print("Pay 00")
else:
    print("The spin resulted in", num, "...\n")
    print("Pay", num,"\n")
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if num in red:
        print("Pay Red\n")
    else:
        print("Pay Black\n")
    if num % 2 == 0:
        print("Pay Even\n")
    else:
        print("Pay Odd\n")
    if num < 19:
        print("Pay 1 to 18\n")
    else:
        print("Pay 19 to 36\n")
