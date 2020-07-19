import random


def randomPassword():
    passLength = random.randrange(7, 11)
    result = ""
    for i in range(passLength):
        result += chr(random.randrange(33, 127))
    return result


def checkPassword(password):
    isLength = False
    isUpper = False
    isLower = False
    isNumber = False
    if len(password) > 7:
        isLength = True
    for c in password:
        if c.isupper():
            isUpper = True
        elif c.islower():
            isLower = True
        elif c.isdigit():
            isNumber = True
    if isLength and isUpper and isLower and isNumber:
        return True
    else:
        return False


def main():
    count = 0
    while 1:
        count += 1
        password = randomPassword()
        if checkPassword(password):
            print("password is {}, try count is {}".format(password, count))
            break


main()
