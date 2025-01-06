def ievadit_recepti():
    print("\nReceptes ievade")
    receptes_sastavdalas = []
    while True:
        sastavdala = input("Ievadiet sastāvdaļas nosaukumu (vai 'beigt'): ")
        if sastavdala.lower() == "beigt":
            break
        daudzums = float(input(f"Ievadiet {sastavdala} daudzumu receptē (kg): "))
        receptes_sastavdalas.append((sastavdala, daudzums))
    return receptes_sastavdalas