isConsonant = False
consonant = ""

onVowel = False
vowels = '''aeiou'''

punctuations = '''!,.?'''
punctuation = ""

isCapital = False
result = ""

string = input('단어를 입력해주세요. ')

for i in range(len(string)):
    c = string[i]
    if c in punctuations:
        punctuation += c
    else:
        if i == 0:
            if c.lower() in vowels:
                onVowel = True
                result += c
            else:
                if c.isupper():
                    isCapital = True
                isConsonant = True
                consonant += c.lower()
        else:
            if onVowel:
                result += c
            else:
                if c in vowels:
                    onVowel = True
                    result += c
                else:
                    consonant += c
if isCapital:
    result = result.capitalize()
if isConsonant:
    print(result + consonant + "ay" + punctuation)
else:
    print(result + "way" + punctuation)