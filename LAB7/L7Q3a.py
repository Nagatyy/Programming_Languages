import itertools
####################    Part 1    ####################
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
####################    Part 2    ####################
def prime_generator(floor = 0):

    current = 2 if floor is 0 else floor + 1

    while True:
        if is_prime(current):
            yield current
        #   for efficiency, we do not want to inc by 1 and go through even numbers
        #   therefore, if the number is even we inc by 1, if it is odd we inc by 2
        current += 1 if current % 2 == 0 else 2
####################    Part 3    ####################
pg = prime_generator()

for i in range(20):
    print(next(pg))

####################    Part 4    ####################
pg = prime_generator() #    to reset pg

list_of_primes = [next(pg) for i in range(20)]
print(list_of_primes)
####################    Part 5    ####################
pg = prime_generator(1_000_000)
list_of_big_primes = list(itertools.islice(pg, 0, 20, 1))
print(list_of_big_primes)
####################    Part 6    ####################
pg = prime_generator(1_000_000)
gen_expression = (next(pg) for x in range(100))

for x in gen_expression:
    print(x)

####################    Part 7    ####################
pg = prime_generator(1_000_000)
gen_expression = (next(pg) for x in range(100))

list_of_special_primes = list(filter(lambda x: x % 10 == int(x/10) % 10, gen_expression))
print(list_of_special_primes)

####################    Part 8    ####################
class Primes:

    def __init__(self, floor=0):
        self.current = 2 if floor is 0 else floor + 1

    def __iter__(self):
        return self

    def __next__(self):

        self.current += 1 if self.current % 2 == 0 else 2

        while not is_prime(self.current):
            self.current += 1 if self.current % 2 == 0 else 2

        return self.current

list_of_class_primes = list(itertools.islice(Primes(1_000_000), 0, 20, 1))

print(list_of_class_primes)








