##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


##############Import modules############################################
# from random import *
# import csv
# import datetime as dt
# import smtplib

# #############################check day########################


# now = dt.datetime.now()
# day = now.date()


# def ler_dados_csv(arquivo):
#     with open(arquivo, "r", newline="") as birthday:
#         leitor_csv = csv.reader(birthday)

#         cabecalho = next(leitor_csv)
#         valores = next(leitor_csv)
        
#         return cabecalho,valores

# def acessar_nome(cabecalho, valores):
#     index_nome = cabecalho.index("name")
#     return valores[index_nome]

# arquivo_csv = "/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY32/birthdays.csv"

# cabecalhos, valores = ler_dados_csv(arquivo_csv)

# nome = acessar_nome(cabecalhos, valores)

# print("Nome do item:", nome)

# num = randint(1,3)

# with open(f"/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY32/letter_templates/letter_{num}.txt") as letter_to_go:
#     name = letter_to_go.read()
#     replace_name = name.replace('[NAME]', nome)
  
# print(replace_name)
    

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#             from_addr=my_email,
#             to_addrs="", 
#             msg=f"Subject:Happy Birthday \n\n{replace_name}")

    


from datetime import datetime
import pandas
import random
import smtplib


MY_EMAIL = ""
MY_PASSWORD = ""

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY32/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmai.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
