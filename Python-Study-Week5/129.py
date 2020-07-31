import random


def rollDice():
    return random.randint(1, 6)


diceList = []
for i in range(1000):
    diceList.append(rollDice() + rollDice())
print("{:>5}".format('Total'), end="   ")
print("{:>9}".format('Simulated'), end="   ")
print("{:>8}".format('Expected'), end="   \n")
print("{:>5}".format(''), end="   ")
print("{:>9}".format('Percent'), end="   ")
print("{:>8}".format('Percent'), end="   \n")

expected = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}
for i in range(2, 13):
    print("{:>5}".format(i), end="   ")
    print("{:>9.2f}".format(diceList.count(i)/10), end="   ")
    print("{:>8}".format(expected.get(i, 'err')), end="   \n")