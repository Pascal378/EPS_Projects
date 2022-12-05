run = True
carte = {"Cola": 100}
carte_list = []

try:
    with open('cart.txt') as f:
        i = 0
        for line in f:
            item = line.replace("\n", "").split(",", 1)
            carte.update({item[0]: item[1]})
            carte_list.append(item[0])
except:
    with open('cart.txt', 'w') as f:
        f.write("")


# Print the carte
def print_carte():
    print("Speisekarte:")
    i = 1
    for x in carte:
        print(str(i) + ". " + x + " - " + str(carte.get(x)))
        i += 1


# Add products to the carte
def add_to_carte():
    print("Bitte tätigen Sie folgende Eingaben. Zum Zurückkehren - b")

    print("Name des Gerichts:")
    name = str(input())
    if name == "b":
        return

    print("Preis des Gerichts:")
    try:
        price = input()
        if price == "b":
            return
        price = int(price)

    except ValueError:
        print("Keine korrekte Eingabe")
        return

    carte.update({name: price})
    carte_list.append(name)

#Delete dish from carte
def delete_from_carte():
    print_carte()
    print("Bitte geben Sie die Nr. des Gerichts ein das sie entfernen moechten.")

    try:
        delete = int(input())
    except ValueError:
        print("Keine Korrekte Eingabe, kehre zurück ins Hauptmenue.")
        return

    if delete > len(carte_list) or delete < 0:
        print("Gericht nicht vorhanden.")
        return
    else:
        carte.pop(carte_list[delete - 1])
        carte_list.remove(carte_list[delete - 1])


# Loop through the menu until user decides to quit
while run:
    print("\nHauptmenü:\n"
          "\n"
          "a = Speisekarte anzeigen\n"
          "n = neues Gericht hinzufügen\n"
          "l = Gericht löschen\n"
          "e = Programmende\n")

    user_input = input()

    if user_input == "a":
        print_carte()
    if user_input == "n":
        add_to_carte()
    if user_input == "l":
        delete_from_carte()
    if user_input == "e":
        with open('cart.txt', 'w') as f:
            for name, price in carte.items():
                f.write('%s,%s\n' % (name, price))
        run = False
