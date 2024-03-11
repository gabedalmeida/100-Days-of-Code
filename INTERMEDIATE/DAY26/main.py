from random import *

# number = [1, 2, 3]
# new_list = []

# for n in number:
#     add = n + 1
#     new_list.append(add)

######/////list comprehension
# new_list = [new_item for item in list]

# new_list = [n+1 for n in number]

# print(new_list)




# new_list = [n*2 for n in range(1,5)]

# print(new_list)

# names = ["Beth", "Alex", "Caroline", "Dave", "Eleanor", "Cla"]
# new_item = []

# short_name_list = [name.upper() for name in names if len(name) > 5]

# print(short_name_list)

# names = ["Beth", "Alex", "Caroline", "Dave", "Eleanor", "Cla"]

# #student_score = {new_key:new_value for item in list}

# student_score = {student:randint(1,100) for student in names}

# #new_dict = {new_key:new_value for (key, value) in dict.items() if test}
# passed_student = {student:score for (student, score) in student_score.items() if score >= 50 }

# print(student_score)

# print(passed_student)



# student_dict = {
#     "student": ["Angela", "Ana", "Gabriel"],
#     "score": [56,76,98]
# }
# student_data_frame = pandas.DataFrame(student_dict)


# # for (key, value) in student_dict.items():
# #     print(key)

# for(index, row) in student_data_frame.iterrows():
#     if row.student == "Gabriel":
#         print(row.score)


import pandas

data = pandas.read_csv("/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:  row.code for (index,row) in data.iterrows()}

word = input("Enter a word:").upper()

output_list = [phonetic_dict[letter] for letter in word]

print(output_list)