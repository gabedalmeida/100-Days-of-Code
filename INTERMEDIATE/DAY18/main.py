# from turtle import Turtle, Screen
# import random
# tt_turtle_obj = Turtle()

# for _ in range(15):
#     tt_turtle_obj.forward(10)
#     tt_turtle_obj.color("white")
#     tt_turtle_obj.forward(10)
#     tt_turtle_obj.color("black")

# screen = Screen()
# screen.exitonclick()

# tim = Turtle()
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_in_n in range(3,11):
#     draw_shape(shape_in_n)
    
# tim = Turtle()
# tim.shape('turtle')
# tim.speed("fastest")
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# direction = [0, 90, 180, 270]

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r, g, b)
#     return color

# for _ in range(200):
#     tim.color(rgb())
#     tim.setheading(random.choice(direction))
#     tim.forward(50)
#     tim.pensize(10)
# tim.speed("fastest")



# def size_draw(size_draw_gap):
#     for _ in range(int(360 / size_draw_gap)):        
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_draw_gap )

# size_draw(10)

# screen = Screen()
# screen.exitonclick()

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()