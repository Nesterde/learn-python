# W tej lekcji wprowadzimy podstawy programowania obiektowego (OOP).

# Tworzymy klasę Osoba
class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie  # Atrybut instancji
        self.wiek = wiek  # Atrybut instancji

    def powitanie(self):
        print(f"Witaj, mam na imię {self.imie} i mam {self.wiek} lat.")

# Tworzymy obiekt klasy Osoba
osoba1 = Osoba("Piotr", 25)

# Wywołujemy metodę obiektu
osoba1.powitanie()
