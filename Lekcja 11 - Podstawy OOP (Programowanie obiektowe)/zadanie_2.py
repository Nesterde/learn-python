# Zadanie 2: Stwórz klasę `Samochod`, która będzie miała atrybuty marka, model,
# rok produkcji oraz metodę `opis`, która wyświetli pełny opis samochodu.

class Samochod:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def opis(self):
        print(f"{self.marka} {self.model}, {self.rok} r.")

# Tworzymy obiekt klasy Samochod
samochod1 = Samochod("Toyota", "Corolla", 2019)

# Wywołujemy metodę
samochod1.opis()
