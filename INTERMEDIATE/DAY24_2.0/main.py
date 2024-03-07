PLACEHOLDER = "[name]"



with open("/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY24_2.0/invited_names.txt") as names_file:
    names = names_file.readlines()
    
    
with open("/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY24_2.0/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        with open(f"/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY24_2.0/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)