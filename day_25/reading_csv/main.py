# Reading data in .csv files
# csv = comma separated values

import csv
import pandas as pd

with open('weather_data.csv', 'r') as data:
    temperatures = []
    datas = csv.reader(data)  # This reads the csv file and returns the data in it in a convenient manner
    # print(datas) This will only return smt like <_csv.reader object at 0x000001BE5AF5FB20>
    for row in datas:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)  # This is the hard way of reading csv files
print('\n')
print('-----------------------------------------------------------------')
print('\n')

# The easy way here :)
data = pd.read_csv('weather_data.csv')
print(data)
print('\n')
print(data['temp'])