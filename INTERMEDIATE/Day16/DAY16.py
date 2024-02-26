# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape('turtle')

# my_screen = Screen()
# timmy.color("black", "red")
# timmy.forward(100)
# timmy.speed()
# print(my_screen)
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu, Squirt, Charmander"])
table.add_column("Type",["Eletric, Water, Fire"])
table.align = "c"


print(table)