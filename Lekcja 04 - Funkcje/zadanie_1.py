# Zadanie 1: Napisz funkcję, która zwróci większą z dwóch liczb.

def wieksza_liczba(a, b):
    if a > b:
        return a
    else:
        return b

# Testujemy funkcję
print(wieksza_liczba(10, 20))  # Powinna zwrócić 20
