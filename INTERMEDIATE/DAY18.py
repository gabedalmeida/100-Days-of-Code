from turtle import Turtle, Screen
import random
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
    
tim = Turtle()
tim.shape('turtle')
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
tim.speed("fastest")



def size_draw(size_draw_gap):
    for _ in range(int(360 / size_draw_gap)):        
        tim.circle(100)
        tim.setheading(tim.heading() + size_draw_gap )

size_draw(10)

    




screen = Screen()
screen.exitonclick()


