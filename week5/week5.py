# import random
#
# for i in range(10):
#     print(random.random())
import turtle


# import random
#
# for i in range(10):
#     print(random.randint(25, 35))

# import math
#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
#
# c = math.sqrt(a**2 + b**2)
#
# print(c)

# import math
#
# def areaofcircle(r):
#     area = math.pi * r**2
#     return area
#
# print(areaofcircle(5))

# import turtle
#
# def drawStar(t, side):
#     for i in range(5):
#         t.forward(side)
#         t.left(144)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# drawStar(tess, 100)
#
# screen.exitonclick()

def drawSquare(t,size):
    for i in range(4):
        t.forward(size)

        t.left(90)
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# tess.color("pink")
# screen.bgcolor("black")
# tess.pensize(5)
# for i in range(5):
#      drawSquare(tess, 20)
#      tess.penup()
#      tess.forward(40)
#      tess.pendown()
# screen.exitonclick()

import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

screen.bgcolor("lightgreen")
tess.color("blue")
tess.pensize(3)

for i in range(20, 120, 20):
    drawSquare(tess, i)
    tess.penup()
    tess.backward(10)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()
screen.exitonclick()