import random
import turtle as t

colors = ["Red", "Green", "Blue"]

tim = t.Turtle()
screen = t.Screen()
##############################
# draw different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
#
#
# for shape_side in range(3, 11):
#     draw_shape(shape_side)


#########################
# draw random pipes
# t.hideturtle()
# t.width(10)
# t.speed(0)
# t.colormode(255)
# angle = [90, 180, 270, 360]
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
# for _ in range(200):
#     t.color(random_color())
#     t.forward(20)
#     t.setheading(random.choice(angle))

#####################
# draw a spirograph
# t.speed(0)
# num_circle = 40
# t.colormode(255)
# for n in range(num_circle):
#     angle = 360 * n / num_circle
#     t.setheading(angle)
#     t.color(random_color())
#     t.circle(100)


screen.exitonclick()






