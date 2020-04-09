def count_range(list, min, max):
   counter = 0
   for x in list:
      if min <= x <= max:
         counter += 1
   return counter

numlist = [1,2,3,4,5,6,7,8,9,10]
print(count_range(numlist, 3, 9))
