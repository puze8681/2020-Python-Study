oneDictionary = {1: 'one', 2: 'two',
         3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight',
         9: 'nine'}
tenDictionary = {1: ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'], 2: 'twenty',
         3: 'thirty', 4: 'forty', 5: 'fifty',
         6: 'sixty', 7: 'seventy', 8: 'eighty',
         9: 'ninety'}

number = input('금액을 입력해주세요. ')
result = ""
isTen = False
count = len(number)
for i in range(0, len(number)):
    c = number[i]
    if c.isdigit():
        if count == 3:
            result = oneDictionary.get(int(c), '') + " hundred "
        elif count == 2:
            if int(c) == 1:
                isTen = True
                result = result + tenDictionary.get(1, '')[int(number[i+1])] + " "
            elif int(c) != 0:
                result = result + tenDictionary.get(int(c), '') + " "
        elif count == 1:
            if not isTen:
                result = result + oneDictionary.get(int(c), '')
        count -= 1
print(result)