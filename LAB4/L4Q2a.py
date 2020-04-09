def enum(lst):
    returnedList = []
    i = 0
    for element in lst:
        returnedList.append((i, element))
        i += 1
    return returnedList


ll = enum(['A', 'B', 'C'])

print(ll)
