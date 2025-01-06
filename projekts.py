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

def ievadit_cenas(receptes_sastavdalas):
    print("\nCenu ievade")
    cenas = {}
    for sastavdala, _ in receptes_sastavdalas:
        cena = float(input(f"Ievadiet cenu par 1 kg {sastavdala} (€): "))
        cenas[sastavdala] = cena
    return cenas