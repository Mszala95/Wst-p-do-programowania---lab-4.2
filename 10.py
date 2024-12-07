def znajdz_wspolne_wartosci(seq1, seq2):

    wspolne = list(set(seq1) & set(seq2))
    return wspolne

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]

wspolne = znajdz_wspolne_wartosci(lista1, lista2)
print(f"Wspólne wartości: {wspolne}")
