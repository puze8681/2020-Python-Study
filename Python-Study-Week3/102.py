def mensuration(number, measure):
    standard = {"cup": 48, "table": 3, "tea": 1}.get(measure, 0)
    teaNumber = number * standard
    cup = teaNumber // 48
    table = (teaNumber % 48) // 3
    tea = ((teaNumber % 48) % 3)
    print("{}컵, {}큰술, {}티스푼".format(cup, table, tea))


mensuration(int(input('단위 수를 입력해주세요. ')), input('측정 단위를 입력하세요. '))