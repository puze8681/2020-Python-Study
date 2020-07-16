# 노래의 구절인 한 개의 숫자를 매개변수로 하는 song 함수 선언
# 함수 내용은 매개변수로 받은 숫자에 해당하는 곡의 구절 속 선물 항목을 출력
# 각 항목은 프로그램에 한 번만 나타나야 하지만 파트리지의 경우는 예외로하여 1절의 항목과 후속절의 항목에 대한 차이를 두어서 출력
# 1부터 12까지의 경우에 해당하는 결과값을 출력, 범위에 대한 예외에는 해당하는 문자열을 출력
# 만약 1절이 아니라면 후속절을 출력
# 반복문을 통해 song 함수를 12번 호출


def song(verse):
    print({1: "A partridge in a pear tree\n", 2: "Two turtle doves", 3: "Three French hens", 4: "Four calling birds", 5: "Five golden ring", 6: "Six geese a laying", 7: "Seven swans a swimming", 8: "Eight maids a milking", 9: "Nine ladies dancing", 10: "Ten lords a leaping", 11: "Eleven pipers piping", 12: "Twelve drummers drumming", }.get(verse, "범위는 1부터 12까지입니다."))
    if verse != 1:
        print("And a partridge in a pear tree.\n")


for i in range(12):
    song(i+1)
