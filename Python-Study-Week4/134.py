chrDictionary = {}
for c in input('문자열을 입력해주세요. '):
    if c != "":
        chrDictionary[c] = c
print(len(chrDictionary))