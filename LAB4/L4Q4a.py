def apply_to_all(func, lst):
    return [] if len(lst) is 0 else [func(lst[0])] + apply_to_all(func, lst[1:])


def sqrt(num):
    return num**(1/2.0)


print(apply_to_all(sqrt, [4, 9, 16, 25]))