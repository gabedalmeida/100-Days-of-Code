from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]

    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letter + password_numbers + password_symbols

# for char in range(nr_letters):
#   password_list.append(choice(letters))

# for char in range(nr_symbols):
#   password_list += choice(symbols)

# for char in range(nr_numbers):
#   password_list += choice(numbers)

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


    print(f"Your password is: {password}")




def save():
    
    website = web_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
        "email": email_username,
        "password": password
        }
    } 
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            
                
        except FileNotFoundError:  
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
            
        else:  
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            
                
    except FileNotFoundError:
        messagebox.showinfo(title="Erro", message="No Data File Found.") 
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
             




window = Tk()
window.title("Password Generate")

window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0,column=1)

image_locked = PhotoImage(file="/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY29/logo.png")
canvas.create_image(100,100, image=image_locked)



#create Label

website = Label(text="website:")
email_username = Label(text="Email/Username:")
password = Label(text="Password:")

#create_button

button_password = Button(width=10, text="Generate Password", command=generate)
button_add = Button(width=33, text="ADD",command=save)
search_button = Button(text="Search", width=13,command=find_password)

# create Entry

web_entry = Entry(width=21)
web_entry.focus()
email_entry = Entry(width=35)
password_entry = Entry(width=21)

email_entry.insert(0," gabealmeida@gmail.com")


#create grid's
website.grid(row=1, column=0)
email_username.grid(row=2,column=0)
password.grid(row=3, column=0)

web_entry.grid(row=1,column=1)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry.grid(row=3,column=1)

button_password.grid(row=3,column=2)
button_add.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2) 



window.mainloop()