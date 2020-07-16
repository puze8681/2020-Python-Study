# 한 개의 숫자를 매개변수로 하는 ordinal 함수 선언
# 함수 내용은 매개변수로 받은 숫자에 해당하는 영어 서수 번호를 포함한 문자열을 출력
# 1부터 12까지의 경우에 해당하는 결과값을 출력, 범위에 대한 예외에는 해당하는 문자열을 출력


def ordinal(number):
    print({1:"1st, first",2:"2nd, second",3:"3rd, third",4:"4th, fourth",5:"5th, fifth",6:"6th, sixth",7:"7th, seventh",8:"8th, eighth",9:"9th, ninth",10:"10th, tenth",11:"11th, eleventh",12:"12th, twelfth",}.get(number, "범위는 1부터 12까지입니다."))


ordinal(int(input('몇번째 순서까지 있는지 입력해주세요. ')))