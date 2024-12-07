#a

def wyswietl_parametry(*args):

    print("Przekazane argumenty:", args)

wyswietl_parametry(1, 2, 3, 4, 5)
wyswietl_parametry("Python", True, 3.14)

#b

def znajdz_maksimum(*args):

    if not args:
        return "Nie podano żadnych argumentów."
    return max(args)

# Przykładowe wywołania funkcji
maks1 = znajdz_maksimum(1, 2, 3, 4, 5)
maks2 = znajdz_maksimum(10, -20, 0, 50)
maks3 = znajdz_maksimum()

print(f"Maksimum z (1, 2, 3, 4, 5): {maks1}")
print(f"Maksimum z (10, -20, 0, 50): {maks2}")
print(maks3)
