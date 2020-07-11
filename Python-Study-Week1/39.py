a = int(input('데시벨을 입력하세요. '))
if a < 40:
    print("Quiet room 보다 작습니다.")
elif a == 40:
    print("Quiet room 과 같습니다.")
elif 40 < a < 70:
    print("Quit room 보다 크고 Alarm clock 보다 작습니다.")
elif a == 70:
    print("Alarm clock 과 같습니다.")
elif 70 < a < 106:
    print("Alarm clock 보다 크고 Gas lawnmower 보다 작습니다.")
elif a == 106:
    print("Gas lawnmower 와 같습니다.")
elif 106 < a < 130:
    print("Gas lawnmower 보다 크고 Jackhammer 보다 작습니다.")
elif a == 130:
    print("Jackhammer 와 같습니다.")
else:
    print("Jackhammer 보다 큽니다.")

