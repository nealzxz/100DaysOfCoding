from replit import clear

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0,
}


def report(t):
    print(f"MENU[t]['ingredients']")
    print(f"MENU[t]['cost']")


def check(t, e):
    for i in MENU[t]['ingredients']:
        if MENU[t]['ingredients'][i] > resources[i]:
            print(f"sorry no {i}")
            e = True
    return e


end_of_use = False
profit = 0

while not end_of_use:
    clear()
    print(resources)
    coffee_type = input("What would you like? (espresso/latte/cappuccino):")
    end_of_use = check(coffee_type, end_of_use)
    if end_of_use:
        print(f'no more {coffee_type}')
    elif coffee_type == 'off':
        end_of_use = True
    else:
        q = int(input("quarter?"))
        d = int(input("dimes?"))
        n = int(input("nickles?"))
        p = int(input("pennies?"))
        total = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
        if total < MENU[coffee_type]['cost']:
            print("We need more money stupid, do it again")
        elif total >= MENU[coffee_type]['cost']:
            resources['profit'] += MENU[coffee_type]['cost']
            print(f"you change is {total - MENU[coffee_type]['cost']}")
            for item in MENU[coffee_type]['ingredients']:
                resources[item] -= MENU[coffee_type]['ingredients'][item]
            print("Here is your coffee,Enjoy!")
