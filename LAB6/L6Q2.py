from functools import reduce
############ Parts a && b #############
def selection_sort(lst):
    if isinstance(lst, list):
        for i in range(len(lst)-1):
            min_index = reduce(lambda a, b: a if lst[a] < lst[b] else b, range(i, len(lst)))
            lst[min_index], lst[i] = lst[i], lst[min_index] if min_index != i else None
    return lst

lst = [1, 2, 3, 4, -2, 8, 1, 100, 0]
print(selection_sort(lst))
