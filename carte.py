run = True
carte = {"Schnitzel": 1000, "Pommes": 200}


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
    price = input()
    if price == "b":
        return

    price = int(price)

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
        run = False
