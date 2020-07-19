import random


def randomPlate():
    result = ""
    for i in range(random.randrange(3, 5)):
        if random.randrange(0, 2):
            result += chr(random.randrange(65, 91))
        else:
            result += chr(random.randrange(97, 123))
    for i in range(3):
        result += str(random.randrange(0, 10))
    print(result)


randomPlate()
