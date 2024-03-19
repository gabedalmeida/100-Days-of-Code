#Types ERROR
# try:
#     file = open("datao.txt")
#     dict ={"key":"value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("datao.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"this {error_message} does not exist")

# else:
#     content = file.read()
#     print(content)
    
# finally:
#     # file.close()
#     # print("This was closed")
#     raise TypeError("This is a error that a made up")

# height = float(input("Height:"))

# if height > 3:
#     raise ValueError("Human height should not be over 3m ")

# weight = int(input("Weight:"))

# bmi = height / weight ** 2

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY30/nato_phoneticalphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        
    except KeyError:
        print("TRY STR")
        generate()
        
    else:
        
        print(output_list)


generate()
