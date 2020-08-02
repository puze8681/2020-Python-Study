digitDictionary = {0: '- - - - -', 1: '.- - - -', 2: '..- - -',
         3: '...- -', 4: '....-', 5: '.....',
         6: '-....', 7: '- -...', 8: '- - -..',
         9: '- - - -.'}
alphaDictionary = {0: '.-', 1: '-...', 2: '-.-.',
         3: '-..', 4: '.', 5: '..-.',
         6: '- -.', 7: '....', 8: '..',
         9: '.- - -', 10: '-.-', 11: '.-..',
         12: '- -', 13: '-.', 14: '- - -',
         15: '.- -.', 16: '- -.-', 17: '.-.', 18: '...',
         19: '-', 20: '..-', 21: '...-',
         22: '.- -', 23: '-..-', 24: '-.- -', 25: '- -..'}
message = input('메시지를 입력해주세요. ')
result = ""
for c in message:
    if c.isalpha():
        upperC = c.upper()
        dif = ord(upperC) - ord("A")
        count = 1
        keyValue = alphaDictionary.get(dif, "")
        if dif > 2:
            for i in range(1, 4):
                if keyValue != alphaDictionary.get(dif-i, ""):
                    break
                count += 1
        else:
            count = (dif % 3) + 1
        result += keyValue * count
    elif c.isdigit():
        result += digitDictionary.get(c, "")
print(result)