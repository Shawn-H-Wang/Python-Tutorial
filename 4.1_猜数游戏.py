from random import randint
'''
a = eval(input("程序预设数为:"))
'''
a = randint(0,9)
x=0
while True:
    x += 1
    i = eval(input("请输入一个0-9的数:"))
    print("这是用户第{}次输入".format(x))
    if i == a:
        print("预测{}次，你猜中了！".format(x))
        break
    elif i < a:
        print("很遗憾，太小了")
    else:
        print("很遗憾，太大了")
