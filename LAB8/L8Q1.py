import random

def random_cipher():
    set1 = random.sample(set(range(1,27)),26)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dictionary = {k: alphabet[v-1] for (k, v) in zip(alphabet, set1)}
    return dictionary

def encode(str):
    lst = [my_dict[x] if x in my_dict else x for x in str]
    return "".join(lst)

def decode(str):
    inv_dict = {v: k for k, v in my_dict.items()}
    lst = [inv_dict[x] if x in inv_dict else x for x in str]
    return "".join(lst)


my_dict = random_cipher()
print(my_dict)
encoded = encode("hellow, world!")
print(encoded)
print(decode(encoded))


