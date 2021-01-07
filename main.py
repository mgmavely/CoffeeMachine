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
    "money": 0,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def off():
    gameState[0] = 0


def get_money():
    money = float(0)
    print("Please insert coins.")
    money += 0.25 * float(input("how many quarters?: "))
    money += 0.10 * float(input("how many dimes?: "))
    money += 0.05 * float(input("how many nickles?: "))
    money += 0.01 * float(input("how many pennies?: "))
    return money


def make(coffee):
    retval = 1
    ing = MENU[coffee]["ingredients"]
    if ing["water"] > resources["water"]:
        retval -= 1
        print("Sorry there is not enough water")
    if coffee != "espresso" and ing["milk"] > resources["milk"]:
        retval -= 1
        print("Sorry there is not enough milk")
    if ing["coffee"] > resources["coffee"]:
        retval -= 1
        print("Sorry there is not enough coffee")
    if retval == 1:
        resources["water"] -= ing["water"]
        if coffee != "espresso":
            resources["milk"] -= ing["milk"]
        resources["coffee"] -= ing["coffee"]
        resources["money"] += MENU[coffee]["cost"]
        return retval
    else:
        return 0


def espresso():
    inp = get_money()
    price = MENU["espresso"]["cost"]
    change = inp - price
    if inp < price:
        print("Sorry that's not enough money.  Money refunded.")
        return
    if make("espresso"):
        if change != 0:
            print(f"Here is your ${round(change,2)} in change")
        print("Here is your espresso ☕ Enjoy!")


def latte():
    inp = get_money()
    price = MENU["latte"]["cost"]
    change = inp - price
    if inp < price:
        print("Sorry that's not enough money.  Money refunded.")
        return
    if make("latte"):
        if change != 0:
            print(f"Here is your ${round(change,2)} in change")
        print("Here is your latte ☕ Enjoy!")


def cappuccino():
    inp = get_money()
    price = MENU["cappuccino"]["cost"]
    change = inp - price
    if inp < price:
        print("Sorry that's not enough money.  Money refunded.")
        return
    if make("cappuccino"):
        if change != 0:
            print(f"Here is your ${round(change,2)} in change")
        print("Here is your cappuccino ☕ Enjoy!")


gameState = [1]
functions = {
    "report": report,
    "off": off,
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,

}


while gameState[0]:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    functions[user_input]()
