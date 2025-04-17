# W tej lekcji omówimy, jak obsługiwać błędy i wyjątki w Pythonie.

# Przykład prostego programu, który może wywołać błąd:
try:
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    wynik = a / b
    print("Wynik dzielenia:", wynik)

# Obsługa błędów
except ZeroDivisionError:
    print("Błąd: Nie można dzielić przez zero!")
except ValueError:
    print("Błąd: Proszę podać poprawne liczby!")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")

# Blok finally będzie wykonany zawsze, niezależnie od tego, czy wystąpił błąd czy nie
finally:
    print("Program zakończony.")
