for i in range(0, 11):
    for j in range(0, 11):
        if i == 0:
            if j == 0:
                print("     ", end="")
            else:
                print("{0:>5d}".format(j), end="")
        else:
            if j == 0:
                print("{0:>5d}".format(i), end="")
            else:
                print("{0:>5d}".format(i*j), end="")
    print("")