import pandas as pd

content = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter: value.code for (key, value) in content.iterrows()}

def nato_output():
    user_input = input("Enter a word: ")
    try:
        nato_phonetic_list = [nato_dict[i.upper()] for i in user_input]
    except KeyError:
        print("Sorry. only letters in the alphabet please.")
        nato_output()
    else:
        print(nato_phonetic_list)

nato_output()