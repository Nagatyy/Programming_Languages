def member(target, lst):

    if len(lst) != 0: #exit condition
        return True if lst[0] == target else member(target, lst[1:])
    else:
        return -1


print(member(5, [1, 2, 3, 4, 5]))
