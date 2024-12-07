def powitanie(imie="Użytkowniku", jezyk="polski"):

    if jezyk == "polski":
        print(f"Cześć, {imie}.")
    elif jezyk == "angielski":
        print(f"Hello, {imie}.")
    elif jezyk == "niemiecki":
        print(f"Guten Morgen, {imie}.")
    else:
        print(f"Witaj, {imie}.")

powitanie("Anna")
powitanie("John", "angielski")
powitanie("Hans", "niemiecki")
powitanie("Luca", "włoski")  # Nieznany język
