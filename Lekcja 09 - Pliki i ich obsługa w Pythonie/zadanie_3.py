# Zadanie 3: Napisz program, który odczyta zawartość pliku, w którym zapisano kilka linii tekstu,
# i wyświetli każdą linię na ekranie.

with open("wielu_linii.txt", "r") as plik:
    linie = plik.readlines()
    for linia in linie:
        print(linia.strip())
