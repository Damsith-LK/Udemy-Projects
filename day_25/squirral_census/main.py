# Figure about how many grey, cinnamon, black squirrels are there in total (Primary Fur Color)
# Save the data into a .csv file named "squirrel_count.csv"

import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinn_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {"Fur Color": ["grey", 'black', 'cinnamon'], "Count": [gray_count, black_count, cinn_count]}
data_frame = pd.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")