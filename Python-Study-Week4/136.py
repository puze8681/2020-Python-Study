string1 = input('문자열1 을 입력해주세요. ')
string2 = input('문자열2 을 입력해주세요. ')

strList1 = []
strList2 = []

for c in string1:
    if c.isalpha():
        strList1.append(c.upper())

for c in string2:
    if c.isalpha():
        strList2.append(c.upper())

strList1.sort()
strList2.sort()

if strList1 == strList2:
    print("아나그램입니다.")
else:
    print("아나그램이 아닙니다.")
print(strList1)
print(strList2)