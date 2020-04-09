def traceFunction(func):
    counter = 0
    def tracing(num):
        nonlocal counter
        print('---' * (counter + 1) + func.__name__ + " " + repr(num))
        counter += 1
        result = func(num)
        print('---' * (counter + 1) + 'return' + " " + repr(result))
        counter -= 1
        return result
    return tracing

def factorial(num):
    return num * factorial(num-1) if num > 0 else 1

def fact(n): return n * fact(n-1) if n>1 else 1

fac = traceFunction(fact) ; fac(7)