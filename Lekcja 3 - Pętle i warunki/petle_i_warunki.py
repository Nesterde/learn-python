# W tej lekcji omówimy pętle oraz warunki w Pythonie.

# Pętla "for" – używamy jej, gdy znamy liczbę iteracji
for i in range(5):  # Iterujemy od 0 do 4
    print("To jest iteracja numer:", i)

# Pętla "while" – używamy jej, gdy chcemy, aby pętla trwała, dopóki spełniony jest warunek
licznik = 0
while licznik < 5:
    print("Pętla while, licznik:", licznik)
    licznik += 1  # Zwiększamy licznik

# Warunki if, elif, else
x = 10
if x < 5:
    print("x jest mniejsze niż 5")
elif x == 10:
    print("x wynosi 10")
else:
    print("x jest większe niż 5 i nie wynosi 10")

# Podsumowanie lekcji:
# - **Pętla "for"**: idealna, gdy znamy liczbę iteracji.
# - **Pętla "while"**: działa dopóki spełniony jest warunek.
# - **Warunki if/elif/else**: pozwalają na wykonanie różnych bloków kodu w zależności od warunku.
