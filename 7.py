def potega_rekurencyjna(a, n):

    if n == 0:  # Każda liczba do potęgi 0 to 1
        return 1
    elif n > 0:  # Rekurencja dla n > 0
        return a * potega_rekurencyjna(a, n - 1)
    else:  # Rekurencja dla n < 0 (liczby ujemne)
        return 1 / potega_rekurencyjna(a, -n)

try:
    a = float(input("Podaj podstawę potęgi (a): "))
    n = int(input("Podaj wykładnik potęgi (n): "))
    wynik = potega_rekurencyjna(a, n)
    print(f"Wynik {a}^{n} wynosi: {wynik:.5f}")
except ValueError:
    print("Podano nieprawidłowe dane. Upewnij się, że podstawę podajesz jako liczbę, a wykładnik jako liczbę całkowitą.")
