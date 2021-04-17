import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3 , n-1)
def snow():
    for i in range(3):
        koch(200,1)
        turtle.left(120)

def main():
    turtle.setup(800,800)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)
    snow()
    #koch(600,3)    #n阶科赫曲线长度、阶数
    turtle.hideturtle()
main()
