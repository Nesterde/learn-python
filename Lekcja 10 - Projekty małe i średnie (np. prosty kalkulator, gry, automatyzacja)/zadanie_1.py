# Zadanie 1: Napisz prosty kalkulator, który obsługuje dodawanie, odejmowanie, mnożenie i dzielenie.

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
dzialanie = input("Wybierz działanie (+, -, *, /): ")

if dzialanie == "+":
    wynik = a + b
elif dzialanie == "-":
    wynik = a - b
elif dzialanie == "*":
    wynik = a * b
elif dzialanie == "/":
    if b != 0:
        wynik = a / b
    else:
        wynik = "Błąd: dzielenie przez zero"
else:
    wynik = "Nieznane działanie"

print("Wynik:", wynik)
