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
    return deck


def shareDeck(deck):
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    print(deck)
    for i in range(0, 20):
        order = i + 1
        if order % 4 == 1:
            player1.append(deck[0])
        elif order % 4 == 2:
            player2.append(deck[0])
        elif order % 4 == 3:
            player3.append(deck[0])
        else:
            player4.append(deck[0])
        del deck[0]
    print(player1)
    print(player2)
    print(player3)
    print(player4)
    print(deck)


shareDeck(shuffle(createDeck()))

