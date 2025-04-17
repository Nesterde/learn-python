# W tej lekcji omówimy funkcje w Pythonie.

# Funkcja to blok kodu, który wykonuje określone zadanie.
# Możemy tworzyć funkcje, aby ponownie używać kodu w różnych miejscach programu.

# Definicja funkcji
def dodaj(a, b):
    return a + b

def powitanie(imie):
    print("Witaj,", imie)

# Wywołanie funkcji
print(dodaj(5, 3))  # Wywołanie funkcji dodaj
powitanie("Piotr")  # Wywołanie funkcji powitanie

# Funkcja z domyślnym argumentem
def witaj(imie="Gość"):
    print("Cześć,", imie)

witaj()  # Używa domyślnej wartości "Gość"
witaj("Anna")  # Używa wartości przekazanej "Anna"

# Podsumowanie lekcji:
# - Funkcje pomagają organizować kod i umożliwiają wielokrotne wykorzystywanie tego samego fragmentu kodu.
# - Możemy przekazywać argumenty do funkcji, a funkcja może zwrócić wynik.
# - Możemy ustawić wartości domyślne dla argumentów funkcji.
