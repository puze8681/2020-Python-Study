digitList = []
num = int(input('정수를 입력하세요. '))
if num > 0:
    for i in range(1, num):
        if num % i == 0:
            digitList.append(i)
    print(digitList)
else:
    print("양의 정수를 입력해주세요.")
