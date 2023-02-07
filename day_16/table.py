from prettytable import PrettyTable


# Building an ASCII table - left aligned
table = PrettyTable()
table.align = 'l'
table.field_names = ['Pokemon Name', 'Type']
table.add_row(['Pikachu', 'Electric'])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Charmander', 'Fire'])
print(table)
print('\n\n')

# Another way to do the same thing but this is center aligned
another_table = PrettyTable()
another_table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmander'])
another_table.add_column('Type', ['Electric', 'Water', 'Fire'])
print(another_table)