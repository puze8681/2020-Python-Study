while 1:
    parity = input("문자열을 입력하세요. ")
    if parity == "":
        break
    else:
        if len(parity) == 8 and parity.count('0') + parity.count('1') == 8:
            if parity.count('1') % 2 == 0:
                print("패리티 비트는 0이어야 합니다.")
            else:
                print("패리티 비트는 1이어야 합니다.")
        else:
            print("8비트를 입력해주세요.")