# W tej lekcji zrobimy prosty kalkulator, który wykonuje podstawowe operacje matematyczne.

# Pobieramy dane od użytkownika
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
dzialanie = input("Jakie działanie chcesz wykonać? (+, -, *, /): ")

# Wykonujemy odpowiednie działanie
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
        wynik = "Nie można dzielić przez zero!"
else:
    wynik = "Nieznane działanie"

# Wyświetlamy wynik
print(f"Wynik: {wynik}")
