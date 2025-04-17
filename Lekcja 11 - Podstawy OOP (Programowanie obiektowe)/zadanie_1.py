# Zadanie 1: Stwórz klasę `Pies`, która będzie miała atrybuty imię, wiek
# oraz metodę `szczekaj`, która wypisuje "Hau hau!".
class Pies:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        print("Hau hau!")

# Tworzymy obiekt klasy Pies
pies = Pies("Reksio", 3)

# Wywołujemy metodę
pies.szczekaj()
