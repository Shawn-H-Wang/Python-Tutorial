from random import random

def printInfo():
    print("该程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0—1之间的小数表示）")

def getInputs():
    a = eval(input("请输入选手A的能力值："))
    b = eval(input("请输入选手B的能力值："))
    n = eval(input("请输入模拟比赛的场次："))
    return a , b , n

def simNGames(pa , pb , n):
    winsA , winsB = 0 , 0
    for i in range(n):
        sorceA , sorceB = simOneGame(pa , pb)
        if sorceA > sorceB:
            winsA += 1
        else:
            winsB += 1
    return winsA , winsB

def simOneGame(pa , pb):
    sorceA , sorceB = 0 , 0
    serve = 'A'
    while not OverGame(sorceA , sorceB):
        if serve == 'A':
            if random() < pa:
                sorceA += 1
            else:
                serve = 'B'
        else:
            if random() < pb:
                sorceB += 1
            else:
                serve = 'A'
    return sorceA , sorceB

def OverGame(a,b):
    return a == 15 or b == 15

def printSummary(a,b):
    n = a + b
    print("一共进行{}场比赛".format(n))
    print("选手A获胜的场次数为{}，获胜的概率为{:.2f}".format(a , a/n))
    print("选手B获胜的场次数为{}，获胜的概率为{:.2f}".format(b , b/n))

def main():
    printInfo()
    probA , probB , n = getInputs()
    winsA , winsB = simNGames(probA , probB , n)
    printSummary(winsA , winsB)    

main()
