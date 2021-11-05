import pandas

data = pandas.read_csv(
    'NATO-alphabet-start/nato_phonetic_alphabet.csv', index_col=0, header=0, squeeze=True).to_dict()

user_name = input("Enter a word: ")
user_name_list = list(user_name.upper())
for letter in user_name_list:
    for (index, row) in data.items():
        if index == letter:
            print(row)
