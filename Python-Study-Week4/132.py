notAlphaDictionary = {'.': '1,', ',': '11', '?': '111', '!': '1111', ':': '11111'}
keyDictionary = {0: '2', 1: '2', 2: '2',
         3: '3', 4: '3', 5: '3',
         6: '4', 7: '4', 8: '4',
         9: '5', 10: '5', 11: '5',
         12: '6', 13: '6', 14: '6',
         15: '7', 16: '7', 17: '7', 18: '7',
         19: '8', 20: '8', 21: '8',
         22: '9', 23: '9', 24: '9', 25: '9'}
message = input('메시지를 입력해주세요. ')
result = ""
for c in message:
    if c.isalpha():
        upperC = c.upper()
        dif = ord(upperC) - ord("A")
        count = 1
        keyValue = keyDictionary.get(dif, "")
        if dif > 2:
            for i in range(1, 4):
                if keyValue != keyDictionary.get(dif-i, ""):
                    break
                count += 1
        else:
            count = (dif % 3) + 1
        result += keyValue * count
    elif c == " ":
        result += "0"
    else:
        result += notAlphaDictionary.get(c, "")
print(result)