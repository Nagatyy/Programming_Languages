def factorial(num):
    def intCheck(num):
        return True if isinstance(num, int) is True else False

    return num * factorial(num-1) if intCheck(num) and num > 0 else 1

def T(n):
    def C(k):
        return factorial(n) / (factorial(k) * factorial(n-k))
    return C

print(T(10)(3))
f = T(10)
print(f(3))