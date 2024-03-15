import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
f = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in f.iterrows()}
# print(dict)
# print(type(f))

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

list_input = list(input("Please enter the word: ").upper())
# print(list_input)

new_list = [dict[letter] for letter in list_input]
print(new_list)
