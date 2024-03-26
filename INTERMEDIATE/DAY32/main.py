import smtplib
import datetime as dt
import random



now = dt.datetime.now()
weekday = now.weekday()

my_email = "?"
password = "vmhzjo-hvfen-gmvmd"


if weekday == 1:
    with open("/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/quotes.txt", "r") as data_file:
        lines = data_file.readlines()
        list_line = []
        for line in lines:
            list_line.append(line)
            
        random_choose = random.choice(list_line)



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="?.com", 
            msg=f"Subject:Monday Motivation\n\n{random_choose}")



