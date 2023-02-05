# Man this became successful than I thought

resources = {
    'Water': {'amount':300, 'unit': 'ml'},
    'Milk': {'amount': 200, 'unit': 'ml'}, 
    'Coffee': {'amount': 100, 'unit': 'g'},
    'Money': {'amount': 0, 'unit': '$'}
}

coffee = {
    'espresso': {'price': 1.50, 'water': 50, 'milk': 0, 'coffee': 18},
    'latte': {'price': 2.50, 'water': 200, 'milk': 150, 'coffee': 24},
    'cappuccino': {'price': 3.00, 'water': 250, 'milk': 100, 'coffee': 24}
}

def show_report():
    for i, ii in resources.items():
        if i != 'Money':
            print(f"{i}: {ii['amount']}{ii['unit']}")
        else:
            print(f'{i}: {ii["unit"]}{ii["amount"]}')

    
def update_report(water, milk, coffee, money):
    """Updates the amounts the resources we have"""
    global resources
    resources['Water']['amount'] -= water
    resources['Milk']['amount'] -= milk
    resources['Coffee']['amount'] -= coffee
    resources['Money']['amount'] += money


def process_coins(quarters, dimes, nickles, pennies):
    money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return money


def check_resources(wanted_water, wanted_milk, wanted_coffee):
    not_enough = []
    left_water = resources['Water']['amount']
    left_milk = resources['Milk']['amount']
    left_coffee = resources['Coffee']['amount']
    
    if left_water < wanted_water:
        not_enough.append('water')
    if left_milk < wanted_milk:
        not_enough.append('milk')
    if left_coffee < wanted_coffee:
        not_enough.append('coffee')
    return not_enough


def check_trans(paid, wanted_amount, coffee):
    # Here paid is process_coins()
    balance = 0
    if paid > wanted_amount:
        balance = paid - wanted_amount
        return [balance, wanted_amount]
    elif paid < wanted_amount:
        return "Sorry, that's not enough money. Money refunded."
    else:
        return [balance, wanted_amount]


def main():

    while True:
        choice = input('What would you like? (espresso, latte, cappuccino): ').lower()

        if choice in coffee.keys():
            ran_out = check_resources(coffee[choice]['water'], coffee[choice]['milk'], coffee[choice]['coffee'])
            if len(ran_out) != 0:
                print(f"Sorry there is not enough {ran_out[0]}")
                continue
            print('Please insert coins.')
            quarters = int(input('how many quarters?: ')) 
            dimes = int(input('how many dimes?: '))
            nickles = int(input('how many nickles?: '))
            pennies = int(input('how many pennies?: '))
            paid = process_coins(quarters, dimes, nickles, pennies)
            trans = check_trans(paid, coffee[choice]['price'], choice)

            if trans == "Sorry, that's not enough money. Money refunded.":
                print(trans)
                continue

            print(f"Here is ${trans[0]} in change.\nHere is your {choice} ☕. Enjoy!")
            update_report(coffee[choice]['water'], coffee[choice]['milk'], coffee[choice]['coffee'], trans[1])

        elif choice == 'report':
            show_report()

        elif choice == 'off':
            break

        else:
            print("Invalid input")
            break


main()