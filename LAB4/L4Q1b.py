def fun(name, address, major):
    return [name[0] + " is studying " + major[0] + " and lives in "\
            + address[0]] + fun(name[1:], address[1:], major[1:])\
            if len(name) != 0 else []

print(fun( ["Ahmed", "John", "Zina"], ["Dubai", "Sharjah", "Al Ain"],
    ["COE", "CMP", "ELE"]))