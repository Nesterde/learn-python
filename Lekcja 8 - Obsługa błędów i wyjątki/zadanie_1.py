# Zadanie 1: Napisz program, który poprosi użytkownika o podanie liczby,
# a następnie spróbuje wykonać dzielenie przez tę liczbę. Obsłuż wyjątek dzielenia przez zero.

try:
    liczba = int(input("Podaj liczbę: "))
    wynik = 100 / liczba
    print("Wynik dzielenia:", wynik)
except ZeroDivisionError:
    print("Błąd: Nie można dzielić przez zero!")
except ValueError:
    print("Błąd: Proszę podać liczbę całkowitą!")
