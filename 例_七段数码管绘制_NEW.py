import turtle , datetime

def drawGap():       #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def drawLine(draw):  #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(d):   #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawDate(date):  #获得要输出的数字
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.color('black')
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.fd(40)
            turtle.color('blue')
        elif i == '+':
            turtle.color('black')
            turtle.write("月",font=("Arial",18,"normal"))
            turtle.fd(40)
            turtle.color('green')
        elif i == '=':
            turtle.color('black')
            turtle.write("日",font=("Arial",18,"normal"))
            turtle.fd(40)
        else:
            drawDigit(eval(i))

def main():
    turtle.hideturtle()
    turtle.setup(800,350,200,200)
    #turtle.speed(pow(2,1000000))
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y-%m+%d='))
main()
