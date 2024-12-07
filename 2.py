def odwracanie_stringa(tekst):

    return tekst[::-1]

tekst_uzytkownika = input("Podaj tekst do odwrócenia: ")
odwrocony_tekst = odwracanie_stringa(tekst_uzytkownika)

print(f"Odwrócony tekst: {odwrocony_tekst}")