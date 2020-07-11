grade = float(input('편지 등급 점수를 입력하세요. '))
if grade < 0:
    print("해당 등급 점수를 가진 편지 등급은 없습니다.")
elif grade > 0:
    gradeList = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]
    dif = abs(grade - 4.0)
    gradeIndex = 0
    for i in range(len(gradeList)):
        if dif > abs(grade - gradeList[i]):
            dif = abs(grade - gradeList[i])
            gradeIndex = i
    print(
        {0: 'A+', 1: 'A-', 2: 'B+', 3: 'B', 4: 'B-', 5: 'C+', 6: 'C', 7: 'C-', 8: 'D+', 9: 'D', 10: 'F'}.get(gradeIndex,
                                                                                                             "해당 편지 등급은 조회할 수 없습니다."))