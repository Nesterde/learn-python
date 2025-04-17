# Zadanie 3: Napisz funkcję, która obliczy średnią z listy liczb.

def srednia(lista):
    return sum(lista) / len(lista)

# Testujemy funkcję
print(srednia([1, 2, 3, 4, 5]))  # Powinna zwrócić 3.0
