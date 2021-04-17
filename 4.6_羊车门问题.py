from random import *
'''
一共三个门
选手随机选一个
主持人打开一个门后为羊的门

对于选手，总结出有三种情况：
第一次：选手选车    主持人开门：羊1或羊2  换：得到羊  不换：得到车
第一次：选手选羊1   主持人开门：羊2       换：得到车  不换：得到羊1
第一次：选手选羊2   主持人开门：羊1       换：得到车  不换：得到羊2

则，逻辑算法为：
    选手在随机选择一扇门后，判断这扇门后是不是车
    如果是车，则不选择换才能够获得奖励
    如果是羊，则选择换才能够获得奖励
    最后看一共进行了多少次试验，并统计：
        不更换答案时获得奖励的次数
        更换答案时获得奖励的次数
    （一次循环即可得出）
'''
door = ['car','sheep1','sheep2']
nochange,change = 0,0
choose = 0
time=int(input("请输入测试次数:"))
for i in range(time):
    shuffle(door) #每一轮游戏时都对门后进行随机调整
    answer = choice(door) #选手随机选择一扇门
    if answer == 'car':
        #nochange 是在不换的情况下获得车的次数
        nochange+=1
    else:
        #change 是在换的情况下获得车的次数
        change+=1
print("不改变答案时获胜的概率:{:.2f}%".format(nochange/time*100))
print("改变了答案时获胜的概率:{:.2f}%".format(change/time*100))

