def apply_select(func, lst):
    return [] if len(lst) == 0 else [lst[0]] + apply_select(func, lst[1:]) if func(lst[0]) else apply_select(func, lst[1:])


def is_odd(num):
    return False if num%2 is 0 else True


print(apply_select( is_odd, [2, 3, 5, 8, 9]))
