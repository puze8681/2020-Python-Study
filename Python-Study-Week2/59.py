plate = input('문자를 입력하세요. ')

if len(plate) == 6 and (plate[0].isalpha() and plate[0].isupper()) and (plate[1].isalpha() and plate[1].isupper()) and (plate[2].isalpha() and plate[2].isupper()) and plate[3].isdigit() and plate[4].isdigit() and plate[5].isdigit():
    print("구형 번호판입니다.")
elif len(plate) == 7 and plate[0].isdigit() and plate[1].isdigit() and plate[2].isdigit() and plate[3].isdigit() and (plate[4].isalpha() and plate[4].isupper()) and (plate[5].isalpha() and plate[5].isupper()) and (plate[6].isalpha() and plate[6].isupper()):
    print("신형 번호판입니다.")
else:
    print("번호판 형식이 유효하지 않습니다.")