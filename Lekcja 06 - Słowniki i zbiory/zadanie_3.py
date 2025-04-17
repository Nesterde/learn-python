# Zadanie 3: Napisz program, który stworzy słownik, w którym kluczami będą numery indeksów,
# a wartościami będą imiona osób. Wydrukuj wszystkie osoby z tego słownika.

slownik = {
    1: "Piotr",
    2: "Anna",
    3: "Marek"
}

for klucz, wartosc in slownik.items():
    print(f"Indeks {klucz}: {wartosc}")
