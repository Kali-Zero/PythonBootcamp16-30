import pandas

nato_data = pandas.read_csv("nato_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

def try_a_word():
    word = input("Enter a word: ").upper()

    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, please only use letters in the alphabet. No numbers or special characters.")
        try_a_word()
    else:
        print(output_list)

try_a_word()

#================Now with added error handling!====================





