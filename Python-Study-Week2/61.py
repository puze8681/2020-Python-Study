count = 0
total = 0
while 1:
    num = int(input("숫자를 입력해주세요. 0을 입력시 평균을 계산합니다. "))
    if num == 0:
        if count == 0:
            print("첫 번째 값을 0으로 입력할 수는 없습니다.")
        else:
            print("평균 :", total/count)
            break
    else:
        count += 1
        total += num