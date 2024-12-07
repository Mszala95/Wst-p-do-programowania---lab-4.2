def oblicz_bmi(waga, wzrost):

    if wzrost <= 0 or waga <= 0:
        return "Błędne dane. Waga i wzrost muszą być większe od zera."

    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        zakres = "niedowaga"
        if bmi < 16:
            podkategoria = "wygłodzenie"
        elif 16 <= bmi < 17:
            podkategoria = "wychudzenie"
        else:
            podkategoria = "niedowaga prawidłowa"
        return bmi, f"{zakres} ({podkategoria})"
    elif 18.5 <= bmi <= 24.9:
        return bmi, "pożądana masa ciała"
    elif 25 <= bmi <= 29.9:
        return bmi, "nadwaga"
    elif 30 <= bmi <= 34.9:
        return bmi, "otyłość I stopnia"
    elif 35 <= bmi <= 39.9:
        return bmi, "otyłość II stopnia"
    else:
        return bmi, "otyłość III stopnia"

waga = float(input("Podaj swoją wagę (kg): "))
wzrost = float(input("Podaj swój wzrost (m): "))

bmi, zakres = oblicz_bmi(waga, wzrost)
print(f"Twoje BMI wynosi {bmi:.2f}. Jesteś w zakresie: {zakres}.")
