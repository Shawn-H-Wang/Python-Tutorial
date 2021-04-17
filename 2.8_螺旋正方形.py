import turtle
length = input()
turtle.left(90)
turtle.pencolor("red")
for i in range(eval(length)):
    turtle.fd(i)
    turtle.left(90)
turtle.seth(0)
