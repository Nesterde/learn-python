# Zadanie 2: Napisz program, który losowo wybierze liczbę i poprosi użytkownika o odgadnięcie jej.

import random

# Losujemy liczbę
liczba = random.randint(1, 100)

# Pobieramy odpowiedź użytkownika
odpowiedz = int(input("Zgadnij liczbę (od 1 do 100): "))

if odpowiedz == liczba:
    print("Brawo, zgadłeś!")
else:
    print(f"Nie zgadłeś. Prawidłowa liczba to {liczba}.")
