import random
max = random.randrange(1, 101)
print(max)
updateCount = 0
for i in range(100):
    temp = random.randrange(1, 101)
    if max < temp:
        max = temp
        print(temp, "<== Update")
        updateCount += 1
    else:
        print(temp)
print("The maximum value found was", max)
print("The maximum value was updated", updateCount, "times")