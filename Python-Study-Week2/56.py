user = input('한 달 동안의 휴대 전화 사용 시간(분) 과 문자 메시지 건수를 입력하세요. ').split()
airTime = int(user[0])
messages = int(user[1])

print("기본 요금 : 15.00$")
total = 15
if airTime > 50:
    addAirTime = (airTime - 50) * 0.25
    total += addAirTime
    print("추가 air time 요금 :", round(addAirTime, 2), "$")
if messages > 50:
    addMessages = (messages - 50) * 0.15
    total += addMessages
    print("추가 text message 요금 :", round(addMessages, 2), "$")
print("911 수수료 : 0.44$")
total += 0.44
tax = total * 0.05
total += tax
print("sales tax :", round(tax, 2), "$")
print("total bill :", round(total, 2), "$")