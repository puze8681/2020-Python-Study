word = input('문자를 입력하세요. ')
isPalindrome = True
for i in (0, len(word) -1):
    if word[i] != word[len(word)-i-1]:
        print("Palindrome 이 아닙니다.")
        isPalindrome = False
        break

if isPalindrome:
    print("Palindrome 이 맞습니다.")