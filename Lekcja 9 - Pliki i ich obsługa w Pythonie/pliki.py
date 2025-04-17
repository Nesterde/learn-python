# W tej lekcji nauczymy się, jak pracować z plikami w Pythonie.

# Zapiszemy dane do pliku
with open("dane.txt", "w") as plik:
    plik.write("To jest przykładowy tekst zapisany do pliku.\n")
    plik.write("Python jest świetnym językiem do automatyzacji.")

# Odczytamy dane z pliku
with open("dane.txt", "r") as plik:
    zawartosc = plik.read()
    print("Zawartość pliku:\n", zawartosc)

# Program otwiera plik w trybie 'w' (write) do zapisu, a następnie w trybie 'r' (read) do odczytu.
