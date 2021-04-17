import turtle
turtle.pencolor("red")
for i in range(4):
    turtle.pencolor("white")
    turtle.fd(50)
    turtle.pencolor("red")
    turtle.fd(150)
    turtle.pencolor("white")
    turtle.fd(50)
    turtle.left(90)
turtle.right(90)
turtle.fd(-50)
