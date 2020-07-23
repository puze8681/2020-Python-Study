import random

selectList = []
lottoList = []
for i in range(6):
    selectList.append(int(input("로또 번호를 입력하세요. ")))
    lottoList.append(random.randint(1, 49))
selectList.sort()
lottoList.sort()
print("선택한 로또 번호: {}\n임의의 로또 번호: {}".format(selectList, lottoList))
count = 0
for n in selectList:
    if n in lottoList:
        count += 1
        print("번호 {}이 중복입니다.".format(n))
if count == 0:
    print("겹치는 로또 번호가 없습니다.")
else:
    print("{}개의 로또 번호가 겹쳤습니다.".format(count))