
# #store in a tuple
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
       
        
# print(add(1,2,3,4,5))

# def calculate(n, **kwargs):
#     # print(kwargs)#dict
#     # for n in kwargs:
#     #     print(kwargs["add"])
#     #     print(kwargs["multiply"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
    
    



# n = int(input("N"))

# add = int(input("N"))

# multiply = int(input("N"))

# calculate(n, add = 2, multiply = 5)



from tkinter import *


# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width="500", height="300")



# # my_label["text"] = "New"
# # my_label.config(text="New")

# def buttom_clicked():
#     my_label = Label(text="What\'s up" ,font=("Arial", 24, "bold"))
#     new_text = input.get()
#     my_label.config(text=input.get())
#     my_label.grid(column=2, row=2)

# button = Button(text="Click me", command=buttom_clicked)
# button.grid(column=0, row=1)

# input = Entry(width=10)
# input.grid(column=1, row=1)
# input.get()
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width="300", height="200")
window.config(padx=20, pady=20)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=0)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()