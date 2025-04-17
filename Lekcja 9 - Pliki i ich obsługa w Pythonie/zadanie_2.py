# Zadanie 2: Napisz program, który poprosi użytkownika o wprowadzenie tekstu i zapisze go do pliku.

tekst = input("Wprowadź tekst do zapisania w pliku: ")

with open("tekst.txt", "w") as plik:
    plik.write(tekst)

print("Tekst zapisany do pliku.")
