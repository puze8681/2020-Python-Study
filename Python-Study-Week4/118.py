import random


def createDeck():
    deck = []
    for j in range(1, 5):
        suit = {1:'s',2:'c',3:'d',4:'h'}.get(j, "null")
        for i in range(1, 14):
            value = {1:'A',10:'T',11:'J',12:'Q',13:'K'}.get(i, str(i))
            deck.append(value+suit)
    return deck


def shuffle(deck):
    for i in range(52):
        base = random.randint(0, 51)
        rebase = random.randint(0, 51)
        temp = deck[base]
        deck[base] = deck[rebase]
        deck[rebase] = temp
    print(deck)


shuffle(createDeck())

