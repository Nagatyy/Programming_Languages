def member(target, lst, index=0):
    return -1 if len(lst) == 0 else index if len(lst) != 0\
        and lst[0] == target else member(target, lst[1:], index + 1)


print(member(5, [1, 2, 3, 4, 5]))

