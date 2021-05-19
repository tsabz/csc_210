def tea_please():
    print("Menu- 1. Mint Tea: $3 per pound | 2. Ginger Tea: $3.50 per pound")
    tea = input("what tea would you like? ")

    if tea == "1":
        mint = int(input("How many pounds of Mint Tea would you like? "))
        amount = mint * 3.00
        print(f'Your total is ${amount}')
    elif tea == "2":
        ginger = int(input("How many pounds of Ginger tea would you like? "))
        amount = ginger * 3.50
        print(f'Your total is ${amount}')


tea_please()
