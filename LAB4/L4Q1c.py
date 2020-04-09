def fun(name, address, major):
    lst = []
    for n,a,m in zip(name, address, major):
        lst.append(n+" from "+m+" lives in "+a)
    return lst


print(fun( ["Ahmed", "John", "Zina"], ["Dubai", "Sharjah", "Al Ain"],
    ["COE", "CMP", "ELE"]))