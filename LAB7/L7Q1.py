def countGenerator():
    a = 0
    while "This lab is a 10/10":    # evaluates to True so...
        yield a
        a += 1
def enumerate(lst):
    return list(zip(countGenerator(), lst))

cg = countGenerator()

for num in range(10):
    print(next(cg))

lst = [0, 10,20,30,40,50]
print(enumerate(lst))



