pointCount = 0
pointList = []
totalDistance = 0
while 1:
    if pointCount == 0:
        x = float(input('Enter the x part of the coordinate: '))
        y = float(input('Enter the y part of the coordinate: '))
        pointList.append((x, y))
        pointCount += 1
    else:
        x = input('Enter the x part of the coordinate: (blank to quit):')
        if x == "":
            # m 은 기울기, b 는 상수
            m = 0
            b = 0
            for i in range(0, len(pointList)-1):
                # 각 좌표를 통해 가장 최적의 기울기와 상수를 구해야 함
                m += 1
                b += 1
            print("y={}x+{}".format(m, b))
            break
        else:
            x = float(x)
            y = float(input('Enter the y part of the coordinate: '))
            pointList.append((x, y))
            pointCount += 1
