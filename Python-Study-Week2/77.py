binary = input('이진수를 입력하세요. ')
total = 0
if binary.isdigit() and len(binary) == (binary.count('0') + binary.count('1')):
    for i in range(len(binary)):
        total += (int(binary[i]) * (2 ** (len(binary) - i -1)))
    print(total)
else:
    print("이진수를 입력해주세요.")
