import turtle
turtle.pencolor("red")
turtle.left(90)
for i in range(6):
    turtle.fd(100)
    turtle.right(60)
turtle.left(60)
for j in range(6):
    for i in range(2):
        turtle.fd(100)
        turtle.right(120)
    turtle.right(180)
