def factorial(num):
    def intCheck(num):
        return True if isinstance(num, int) is True else False

    return num * factorial(num-1) if intCheck(num) and num > 0 else 1

print(factorial(5))





