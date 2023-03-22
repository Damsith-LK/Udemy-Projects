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
temps = data['temp']
print(temps)
print('\n -------------------------------------------------------------------- \n')


# Challenge 1 - Calculate the average temperature
temp_list = temps.to_list()
average = round(sum(temp_list) / len(temp_list), 3)
print(f"The average of the temperatures is {average}")

# Can be done lot easier
print(f"In the easier way: {round(temps.mean(), 3)}")
print('\n--------------------------------------------------------------------------\n')


# Challenge 2 - Get the maximum value of temperatures
print(f"The maximum value of temperatures is {temps.max()}")
print('\n--------------------------------------------------------------------------\n')


# Challenge 3 - Print the row of data which has the highest temperature
print(data[data.temp == data['temp'].max()])
print('\n--------------------------------------------------------------------------\n')


# Challenge 4 - Convert Monday's temperature to Fahrenheit
monday_temp = data[data.day == "Monday"].temp
print(monday_temp * 1.8 + 32)
print('\n--------------------------------------------------------------------------\n')


# Creating a data frame from a dict
anime_dict = {
    "animes": ["Demon Slayer", "Attack on Titan", "One Piece", "One Punch Man", "Jujutsu Kaisen"],
    "Main Characters": ["Tanjiro", "Eren", "Luffy", "Saitama", "Itadori"]
}
data_frame = pd.DataFrame(anime_dict)
print(data_frame)