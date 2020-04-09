def enum(lst, start=0, step=1):
    returnedList = []
    i = start
    for element in lst:
        returnedList.append((i, element))
        i += step
    return returnedList


ll = enum(['A', 'B', 'C'], 4, 2)

print(ll)