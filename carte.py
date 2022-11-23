run = True
carte = {"Cola": 100}

with open('cart.txt') as f:
    for line in f:
        current = line.replace("\n", "")
        item = current.split(":", 1)
        carte.update({item[0]: item[1]})


# Print the carte
def print_carte():
    print("Speisekarte:")
    for x in carte:
        print(x + " - " + str(carte.get(x)))


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
        print("Nicht erlaubte Eingabe")

    carte.update({name: price})


# Loop through the menu until user decides to quit
while run:
    print("\nHauptmenü:\n"
          "\n"
          "a = Speisekarte anzeigen\n"
          "n = neues Gericht hinzufügen\n"
          "e = Programmende")
    userInput = input()

    if userInput == "a":
        print_carte()
    if userInput == "n":
        add_to_carte()
    if userInput == "e":
        with open('cart.txt', 'w') as f:
            for name, price in carte.items():
                f.write('%s:%s\n' % (name, price))
        run = False
