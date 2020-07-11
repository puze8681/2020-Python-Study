for i in range(1, 6):
    original = (i * 5) - 0.05
    discount = original * 0.6
    new = original * 0.4
    original = str(round(original, 2)) +'$'
    discount = str(round(discount, 2)) +'$'
    new = str(round(new, 2)) +'$'
    print(original, discount, new)
