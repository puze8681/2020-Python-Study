codeDictionary = {'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick', 'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec', 'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario', 'R': 'Manitoba', 'S': 'Saskatchewan', 'T': 'Alberta', 'V': 'British Columbia', 'X': 'Nunavut or Northwest Territories', 'Y': 'Yukon'}
postal = input('우편번호를 입력해주세요. ')
print(codeDictionary.get(postal[0].upper(), "유효하지 않은 우편번호입니다."))
if codeDictionary.get(postal[0].upper()):
    if postal[1] == '0':
        print("시골 주소를 위한 것입니다.")
    else:
        print("도시 주소를 위한 것입니다.")
