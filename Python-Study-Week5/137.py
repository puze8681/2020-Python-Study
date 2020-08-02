oneList = ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U']
twoList = ['D', 'G']
threeList = ['B', 'C', 'M', 'P']
fourList = ['F', 'H', 'V', 'W', 'Y']
fiveList = ['K']
eightList = ['J', 'X']
tenList = ['Q', 'Z']

pointDictionary = {1: oneList, 2: twoList, 3: threeList, 4: fourList, 5: fiveList, 8: eightList, 10: tenList}

word = input('단어를 입력해주세요. ').upper()
point = 0
for c in word:
    for i in range(1, 11):
        if c in pointDictionary.get(i, []):
            point += i
print(point)