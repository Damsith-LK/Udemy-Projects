import pandas as pd

content = pd.read_csv("nato_phonetic_alphabet.csv")

user_input = input("Enter a word: ")
nato_dict = {value.letter: value.code for (key, value) in content.iterrows()}
nato_phonetic_list = [nato_dict[i.upper()] for i in user_input if i.upper() in nato_dict.keys()]
print(nato_phonetic_list)