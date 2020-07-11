approximations = 3
for i in range(1, 16):
    term = 4 / ((i * 2) * ((i * 2) + 1) * ((i * 2) + 2))
    if i % 2 == 0:
        approximations -= term
    else:
        approximations += term
print(approximations)