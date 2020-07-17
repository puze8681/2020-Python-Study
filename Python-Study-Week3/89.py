def capitalize(original):
    result = ""
    punctuations = '''!,.?'''
    isEnd = True
    for i in range(len(original)):
        c = original[i]
        if c in punctuations:
            isEnd = True
            result = result + c
        else:
            if isEnd and c.isalpha():
                result = result + c.upper()
                isEnd = False
            else:
                if c == 'i' and i != 0:
                    if original[i-1] == original[i+1] == ' ':
                        result = result + c.upper()
                    else:
                        result = result + c
                else:
                    result = result + c
    print(result)


capitalize(input('문자열을 입력하세요. '))
