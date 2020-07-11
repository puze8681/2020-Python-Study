pointCount = 0
pointList = []
totalDistance = 0
while 1:
    if pointCount == 0:
        x = int(input('Enter the x part of the coordinate: '))
        y = int(input('Enter the y part of the coordinate: '))
        pointList.append((x, y))
        pointCount += 1
    else:
        x = input('Enter the x part of the coordinate: (blank to quit):')
        if x == "":
            for i in range(0, len(pointList)):
                if i == len(pointList)-1:
                    totalDistance += (((pointList[i][0] - pointList[0][0]) ** 2) + ((pointList[i][1] - pointList[0][1]) ** 2)) ** 0.5
                    break
                else:
                    totalDistance += (((pointList[i][0] - pointList[i+1][0]) ** 2) + ((pointList[i][1] - pointList[i+1][1]) ** 2)) ** 0.5
            print("The perimeter of that polygon is", totalDistance)
            break
        else:
            y = int(input('Enter the y part of the coordinate: '))
            pointList.append((int(x), y))
            pointCount += 1
