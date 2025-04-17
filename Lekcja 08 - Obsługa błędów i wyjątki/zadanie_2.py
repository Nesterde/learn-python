# Zadanie 2: Napisz program, który zapyta użytkownika o imię i wiek.
# Obsłuż błędy związane z niepoprawnym wiekiem (np. jeśli użytkownik poda tekst).

try:
    imie = input("Podaj swoje imię: ")
    wiek = int(input("Podaj swój wiek: "))
    print(f"Twoje imię to {imie}, a Twój wiek to {wiek}.")
except ValueError:
    print("Błąd: Wiek musi być liczbą całkowitą.")
