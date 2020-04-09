from functools import reduce
fahrenheit_temps = [10, 20, 30, 40, 50, 60, 70]

##################### 1 #####################
celsius_temps = list(map(lambda n: round(5.0/9 * (n-32), 2), fahrenheit_temps))
print(celsius_temps)
##################### 2 #####################
celsius_temps = []
celsius_temps = [round(5.0/9 * (n-32), 2) for n in fahrenheit_temps]
print(celsius_temps)
##################### 3 #####################
avg = round(reduce(lambda a, b: a + b, celsius_temps)/len(celsius_temps), 2)
print(avg)
##################### 4 #####################
list_of_variance_components = list(map(lambda x: round((x - avg)**2, 2), celsius_temps))
print(list_of_variance_components)
##################### 5 #####################
std = round((reduce(lambda a, b: a + b, list_of_variance_components)/len(celsius_temps))**0.5,2)
print(std)
##################### 5 #####################
negative_temps = list(filter(lambda n: n if n < 0 else None, celsius_temps))
print(negative_temps)





