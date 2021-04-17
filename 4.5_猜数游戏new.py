from random import randint
x=0
a = randint(0,9)
while True:
    try:
        i = int(input("请输入一个整数:"))
    except:
        print("错误！请输入一个整数！")
        #break
    else:
        x += 1
        print("这是用户第{}次正确输入".format(x))
        if i == a:
            print("预测{}次，你猜中了！".format(x))
            break
        elif i < a:
            print("很遗憾，太小了")
        else:
            print("很遗憾，太大了")
print("Program End")
