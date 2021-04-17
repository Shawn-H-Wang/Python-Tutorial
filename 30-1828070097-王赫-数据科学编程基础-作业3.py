from random import randint

#创建含有指定元素的列表
def makeLs():
    ls = []
    ls += " "
    for i in (65,97):
        for j in range(26):
            ls += chr(i+j)
    for i in range(10):
        ls += str(i)
    return ls

#判断条件（3）
def Judge(a,s):
    count = 0
    if len(a) > len(s):
        return 0 , False
    else:
        for i in range(len(a)):
            if a[i] == s[i]:
                count += 1
        return count , True

#游戏玩法
def Play(ls):
    s=""
    length = randint(1,15)
    for i in range(length):
        s += ls[randint(0,62)]
    print(s)
    a = input()
    count , j = Judge(a,s)
    if j:
        print("本次的正确率是{:.2f}%".format(count/len(s)*100))
        return count/len(s)*100 , True
    else:
        print("你输入的字符串超长，无效。")
        return 0 , False

#开始游戏
def Game():
    ls = makeLs()
    count=0
    rate = 0
    try:
        n = eval(input("请输入打字次数："))
    except NameError:
        print("输入错误，请输入一个整数！")
    except:
        print("其他错误！")
    else:
        while True:
            print()
            r,j = Play(ls)
            if j:
                count += 1
                rate += r
            else:
                continue
            if count >= n:
                break
        print("整体的正确率：{:.2f}%".format(rate/n))

Game()
