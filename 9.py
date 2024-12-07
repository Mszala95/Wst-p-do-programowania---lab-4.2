def fibonacci(n):

    if n < 0:
        return "Indeks nie może być ujemny."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    n = int(input("Podaj indeks wyrazu ciągu Fibonacciego (n >= 0): "))
    wynik = fibonacci(n)
    print(f"{n}-ty wyraz ciągu Fibonacciego to: {wynik}")
except ValueError:
    print("Podano nieprawidłowe dane. Upewnij się, że podajesz liczbę całkowitą.")
