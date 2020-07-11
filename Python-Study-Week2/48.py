year = int(input('년도를 입력하세요. '))
if year < 0:
    print("0보다 작은 수는 입력할 수 없습니다.")
else:
    print({0:'Monkey', 1:'Rooster', 2:'Dog', 3:'Pig', 4:'Rat', 5:'Ox', 6:'Tiger', 7:'Hare',8:'Dragon', 9:'Snake', 10:'Horse', 11:'Sheep'}.get(year%12, "Err"))