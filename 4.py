def oblicz_srednia(liczby):

    if not liczby:
        return 0
    return sum(liczby) / len(liczby)

lista_liczb = [10, 20, 30, 40, 50]
srednia = oblicz_srednia(lista_liczb)

print(f"Średnia z liczb {lista_liczb} wynosi {srednia:.2f}.")
