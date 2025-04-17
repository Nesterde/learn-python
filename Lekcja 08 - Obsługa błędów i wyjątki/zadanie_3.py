# Zadanie 3: Napisz program, który pyta użytkownika o liczbę, a następnie
# wykonuje dzielenie przez 0. Pokaż odpowiedni komunikat, gdy wystąpi wyjątek.

try:
    liczba = int(input("Podaj liczbę: "))
    wynik = 10 / liczba
except ZeroDivisionError:
    print("Błąd: Próba dzielenia przez zero!")
else:
    print("Wynik dzielenia:", wynik)
finally:
    print("Program zakończony.")
