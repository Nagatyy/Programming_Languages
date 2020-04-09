def fun(name, address, major):
    lst = []
    for i in range(len(name)):
        lst.append(name[i] + " from " + major[i] + " lives in " + address[i])
    return lst


print(fun( ["Ahmed", "John", "Zina"], ["Dubai", "Sharjah", "Al Ain"],
    ["COE", "CMP", "ELE"] ))
