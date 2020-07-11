q = input('십진수를 입력하세요. ')
result = list("")
if q.isdigit():
    q = int(q)
    while 1:
        r = q%2
        result.insert(0, str(r))
        q = q//2
        if q == 0:
            break
    print(''.join(result))
else:
    print("십진수를 입력해주세요.")
