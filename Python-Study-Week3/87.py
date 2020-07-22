def center(string, width):
    if width < len(string):
        return string
    else:
        return " " * width + string


center(input('문자열을 입력해주세요. '), int(input('단자의 너비를 입력해주세요.')))
