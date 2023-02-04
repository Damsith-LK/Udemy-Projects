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
    resources['Water']['amount'] -= water
    resources['Milk']['amount'] -= milk
    resources['Coffee']['amount'] -= coffee
    resources['Money']['amount'] += money


show_report()
update_report(100, 100, 50, 100)
show_report()
# while True:
#     user = input('What would you like? (espresso, latte, cappuccino): ')
