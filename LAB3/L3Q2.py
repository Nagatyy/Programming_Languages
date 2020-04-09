

L = []
for x in range(1,6):
	L.append((x*10, x*10, x*10))

print(L)

print("After removing : ")
L.pop()
print(L)

print("inserting before last: ")
h = 111, 64, 45
L.insert(len(L) - 1, h)
print(L)


print('{0:>10}{1:>10}{2:>10}'.format('X', 'Y', 'Z'))
for x, y, z in L:
    print('{0:>10}{1:>10}{2:>10}'.format(x, y, z))
