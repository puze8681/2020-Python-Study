m = int(input('정수 m 을 입력해주세요. '))
n = int(input('정수 n 을 입력해주세요. '))
d = m

if m > n:
    d = n

while 1:
    if m % d == 0 and n % d == 0:
        print("두 수의 최대공약수는", d)
        break
    else:
        d -= 1