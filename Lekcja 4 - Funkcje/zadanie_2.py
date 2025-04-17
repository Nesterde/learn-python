# Zadanie 2: Napisz funkcję, która sprawdzi, czy liczba jest parzysta, czy nie.

def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

# Testujemy funkcję
print(czy_parzysta(4))  # Powinna zwrócić True
print(czy_parzysta(7))  # Powinna zwrócić False
