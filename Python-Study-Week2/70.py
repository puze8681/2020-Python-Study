message = input('암호화 혹은 해독할 메시지를 입력하세요. ')
shift = int(input('이동할 값을 입력하세요. '))
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = ""
for i in range(len(message)):
    if message[i].isupper():
        index = upper.index(message[i])
        result += upper[(index + shift) % 26]
    else:
        index = lower.index(message[i])
        result += lower[(index + shift) % 26]
print(result)