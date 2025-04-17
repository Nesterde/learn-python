# Zadanie 3: Napisz prostą grę, która zapyta użytkownika o jego imię i wiek,
# a następnie wydrukuje komunikat powitalny i oceni wiek użytkownika.

imie = input("Jak masz na imię? ")
wiek = int(input("Ile masz lat? "))

print(f"Witaj {imie}!")

if wiek < 18:
    print("Jesteś niepełnoletni.")
else:
    print("Jesteś pełnoletni.")
