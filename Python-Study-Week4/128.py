def reverseLookup(data, key):
    if key.isdigit():
        print("찾는 값은 {}".format(data.get(int(key), "없습니다.")))
    else:
        print("키 값은 숫자입니다.")


data = {1:"1st, first",2:"2nd, second",3:"3rd, third",4:"4th, fourth",5:"5th, fifth",6:"6th, sixth",7:"7th, seventh",8:"8th, eighth",9:"9th, ninth",10:"10th, tenth",11:"11th, eleventh",12:"12th, twelfth",}
reverseLookup(data, input("키 값을 입력해주세요. "))
