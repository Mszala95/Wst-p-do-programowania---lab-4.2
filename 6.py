import math

def oblicz_pole_trojkata(a, b, c):

    try:
        # Sprawdzenie poprawności danych
        a, b, c = float(a), float(b), float(c)
        if a <= 0 or b <= 0 or c <= 0:
            return "Boki trójkąta muszą być dodatnie."
        if a + b <= c or a + c <= b or b + c <= a:
            return "Nie można utworzyć trójkąta z podanych boków."

        # Obliczanie pola trójkąta wzorem Herona
        s = (a + b + c) / 2  # Półobwód
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return f"Pole trójkąta wynosi: {pole:.2f}"

    except ValueError:
        return "Podano nieprawidłowe dane. Upewnij się, że podajesz liczby."


a = input("Podaj długość boku a: ")
b = input("Podaj długość boku b: ")
c = input("Podaj długość boku c: ")

wynik = oblicz_pole_trojkata(a, b, c)
print(wynik)
