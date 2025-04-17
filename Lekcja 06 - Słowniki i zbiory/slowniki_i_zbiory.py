# W tej lekcji omówimy słowniki i zbiory w Pythonie.

# Słownik to kolekcja, która przechowuje dane w postaci par klucz-wartość.
slownik = {
    "imie": "Piotr",
    "wiek": 25,
    "miasto": "Warszawa"
}

# Odwołanie do wartości po kluczu
print("Imię:", slownik["imie"])
print("Wiek:", slownik.get("wiek"))

# Można dodać nową parę klucz-wartość
slownik["zawod"] = "Programista"
print("Zawód:", slownik["zawod"])

# Zbiory (sets) to kolekcje, które przechowują unikalne elementy (bez duplikatów).
zbior = {1, 2, 3, 4, 5}
print("Zbiór:", zbior)

# Dodanie elementu do zbioru
zbior.add(6)
print("Zbiór po dodaniu elementu:", zbior)

# Podsumowanie lekcji:
# - **Słowniki** przechowują dane w postaci par klucz-wartość, gdzie klucze są unikalne.
# - **Zbiory** przechowują unikalne elementy, nie pozwalając na duplikaty.
