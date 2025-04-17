# Zadanie 1: Napisz program, który zapisze Twoje imię i nazwisko do pliku, a następnie je odczyta.

with open("dane_osoby.txt", "w") as plik:
    plik.write("Jan Kowalski")

with open("dane_osoby.txt", "r") as plik:
    zawartosc = plik.read()
    print("Zawartość pliku:", zawartosc)
