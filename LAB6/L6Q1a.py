def to_celsius(fahrenheit):
    return round(5.0/9 * (fahrenheit-32),2)

fahrenheit_temps = [10, 20, 30, 40, 50, 60, 70]
celsius_temps = list(map(to_celsius, fahrenheit_temps))

print(celsius_temps)