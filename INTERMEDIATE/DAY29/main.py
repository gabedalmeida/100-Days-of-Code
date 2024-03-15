from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


#Password Generator Project

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
pyperclip.copy(password)

print(f"Your password is: {password}")


window = Tk()
window.title("Password Generate")

window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
canvas.grid(row=0,column=1)

image_locked = PhotoImage(file="/Users/gabrielalmeida/Desktop/Projetos/100-Days-of-Code/INTERMEDIATE/DAY29/logo.png")
canvas.create_image(100,100, image=image_locked)


def save():
    
    website = web_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()
    
    
    if len(website) == 0 or len(password):
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username}\nPassword: {password}\n Is it ok to save?")
    
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email_username} | {password}\n ")
                web_entry.delete(0, END)
                password_entry.delete(0, END)









#create Label

website = Label(text="website:")
email_username = Label(text="Email/Username:")
password = Label(text="Password:")

#create_button

button_password = Button(width=10, text="Generate Password")
button_add = Button(width=33, text="ADD",command=save)

# create Entry

web_entry = Entry(width=35)
web_entry.focus()
email_entry = Entry(width=35)
password_entry = Entry(width=20)
password_entry.insert(0,f"{password}")
email_entry.insert(0," gabealmeida@gmail.com")


#create grid's
website.grid(row=1, column=0)
email_username.grid(row=2,column=0)
password.grid(row=3, column=0)

web_entry.grid(row=1,column=1,columnspan=2)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry.grid(row=3,column=1)

button_password.grid(row=3,column=2)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()