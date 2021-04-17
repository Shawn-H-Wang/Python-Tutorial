from random import randint

def makeLs():
    ls = []
    ls += " "
    for i in (65,97):
        for j in range(26):
            ls += chr(i+j)
    for i in range(10):
        ls += str(i)
    return ls

def Judge(a,s):
    count = 0
    if len(a) > len(s):
        return 0 , False
    else:
        for i in range(len(a)):
            if a[i] == s[i]:
                count += 1
        return count , True

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

def Game():
    ls = makeLs()
    count=0
    rate = 0
    n = eval(input("请输入打字次数："))
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
