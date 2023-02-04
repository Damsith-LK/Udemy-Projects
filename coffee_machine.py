resources = {
    'Water': {'amount':300, 'unit': 'ml'},
    'Milk': {'amount': 200, 'unit': 'ml'}, 
    'Coffee': {'amount': 76, 'unit': 'g'},
    'Money': {'amount': 0, 'unit': '$'}
}
prices = {''}


def show_report():
    for i, ii in resources.items():
        print(f"{i}: {ii['amount']}{ii['unit']}")

    
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


def check_trans(paid, wanted_amount):
    balance = 0
    if paid > wanted_amount:
        balance = paid - wanted_amount
        return balance
    elif paid < wanted_amount:
        return 'bad'
    else:
        return balance


# while True:
#     user = input('What would you like? (espresso, latte, cappuccino): ')
