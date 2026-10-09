# for i in range(100):
#     print("We like python's turtles!")

# months = ["january" , "february" , "march" , "april" , "may" , "june" "july" , "august" , "september" , "october" ,"november" , "december"]
# for month in months:
#     print("One of the months of the year is", month)

# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for number in numbers:
#     print(number)

# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for number in numbers:
#     print(number,"squared is" ,number**2)

# import turtle
#
# t = turtle.Turtle()
# screen=turtle.Screen()
#
# t.penup()
# t.goto(-200, 0)
# t.pendown()
# for i in range(3):
#     t.forward(80)
#     t.left(120)
# t.penup()
# t.goto(-100,0)
# t.pendown()
# for i in range(4):
#     t.forward(80)
#     t.left(90)
#
# t.penup()
# t.goto(20,0)
# t.pendown()
# for i in range(6):
#     t.forward(43)
#     t.left(60)
# t.penup()
#
# t.goto(0, -200)
# t.pendown()
# for i in range(8):
#     t.forward(35)
#     t.left(45)
# t.penup()
# (screen.exitonclick())

import turtle

screen = turtle.Screen()
screen.bgcolor("Lightpink")

t = turtle.Turtle()
t.shape("turtle")
t.color("turquoise")
t.pensize(3)

t.stamp()
t.penup()

for i in range(12):
    t.forward(125)
    t.pendown()
    t.forward(15)
    t.penup()
    t.forward(25)
    t.stamp()
    t.backward(165)
    t.left(30)
screen.exitonclick()