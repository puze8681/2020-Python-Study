import random


def randomPassword():
    passLength = random.randrange(7, 11)
    print(passLength)
    result = ""
    for i in range(passLength):
        result += chr(random.randrange(33, 127))
    print(result)


randomPassword()
