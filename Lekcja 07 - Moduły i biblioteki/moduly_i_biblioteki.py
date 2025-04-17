# W tej lekcji omówimy, jak korzystać z modułów i bibliotek w Pythonie.

# Aby użyć funkcji z modułu, musimy go najpierw zaimportować.
import math  # Importujemy bibliotekę matematyczną

# Korzystamy z funkcji biblioteki math
print("Pierwiastek z 16 to:", math.sqrt(16))
print("Liczba pi to:", math.pi)

# Możemy również zaimportować określoną funkcję z modułu
from math import pow

# Używamy tylko tej jednej funkcji
print("2 podniesione do potęgi 3 to:", pow(2, 3))

# Możemy także tworzyć własne moduły.
# Załóżmy, że stworzyliśmy plik `matematyka.py` z funkcją dodawania:
# from matematyka import dodaj
# print(dodaj(3, 5))  # Powinniśmy uzyskać wynik 8.

# Podsumowanie lekcji:
# - Moduły i biblioteki w Pythonie pozwalają na ponowne wykorzystanie kodu.
# - Możemy używać gotowych funkcji i narzędzi, co upraszcza programowanie.
