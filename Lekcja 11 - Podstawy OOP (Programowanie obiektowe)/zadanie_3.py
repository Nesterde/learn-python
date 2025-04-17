# Zadanie 3: Stwórz klasę `KontoBankowe`, która będzie miała atrybuty
# numer konta i saldo. Dodaj metodę `wplata`, która doda pieniądze do salda,
# oraz metodę `wyplata`, która zdejmie pieniądze z konta (jeśli jest wystarczająco
# dużo środków).

class KontoBankowe:
    def __init__(self, numer_konta, saldo):
        self.numer_konta = numer_konta
        self.saldo = saldo

    def wplata(self, kwota):
        self.saldo += kwota
        print(f"Na konto wpłynęło {kwota} zł. Aktualne saldo: {self.saldo} zł.")

    def wyplata(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            print(f"Wyjęto {kwota} zł. Aktualne saldo: {self.saldo} zł.")
        else:
            print("Błąd: Brak wystarczających środków.")

# Tworzymy obiekt klasy KontoBankowe
konto = KontoBankowe("1234567890", 1000)

# Testujemy metody
konto.wplata(500)
konto.wyplata(300)
