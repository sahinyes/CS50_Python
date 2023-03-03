def taqo():
    cash = 0
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    while True:
        try:
            a = input("Item: ").title()
            if a in menu:
                cash += menu[a]
                print(f"Total: $",f"{cash:.2f}", sep="")
        except:
            return taqo

taqo()
