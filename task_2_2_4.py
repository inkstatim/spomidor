def fahrenheit_to_celsius(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    return c

f= 100

print(f'"{f} градусов по Фаренгейту равняется {round(fahrenheit_to_celsius(f), 2)} по Цельсию".')