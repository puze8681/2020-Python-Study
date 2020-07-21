def magicDate():
    for year in range(1901, 2001):
        for month in range(1, 13):
            if month == 2:
                if year % 400 == 0:
                    limit = 29
                elif year % 100 == 0:
                    limit = 28
                elif year % 4 == 0:
                    limit = 29
                else:
                    limit = 28
            else:
                limit = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}.get(month, 0)
            for date in range(1, limit+1):
                if year % 100 == month * date:
                    print("magic date: {}-{}-{}".format(year, month, date))


magicDate()