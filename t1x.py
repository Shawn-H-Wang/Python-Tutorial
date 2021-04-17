from random import randint                               #1
                                                         #2
def makeLs():                                            #3
    ls = []                                              #4
    ls += " "                                            #5
    for i in (65,97):                                    #6
        for j in range(26):                              #7
            ls += chr(i+j)                               #8
    for i in range(10):                                  #9
        ls += str(i)                                     #10
    return ls                                            #11
                                                         #12
def Judge(a,s):                                          #13
    count = 0                                            #14
    if len(a) > len(s):                                  #15
        return 0 , False                                 #16
    else:                                                #17
        for i in range(len(a)):                          #18
            if a[i] == s[i]:                             #19
                count += 1                               #20
        return count , True                              #21
                                                         #22
def Play(ls):                                            #23
    s=""                                                 #24
    length = randint(1,15)                               #25
    for i in range(length):                              #26
        s += ls[randint(0,62)]                           #27
    print(s)                                             #28
    a = input()                                          #29
    count , j = Judge(a,s)                               #30
    if j:                                                #31
        print("本次的正确率是{:.2f}%".format(count/len(s)*100)) #32
        return count/len(s)*100 , True                   #33
    else:                                                #34
        print("你输入的字符串超长，无效。")                           #35
        return 0 , False                                 #36
                                                         #37
def Game():                                              #38
    ls = makeLs()                                        #39
    count=0                                              #40
    rate = 0                                             #41
    n = eval(input("请输入打字次数："))                          #42
    while True:                                          #43
        print()                                          #44
        r,j = Play(ls)                                   #45
        if j:                                            #46
            count += 1                                   #47
            rate += r                                    #48
        else:                                            #49
            continue                                     #50
        if count >= n:                                   #51
            break                                        #52
    print("整体的正确率：{:.2f}%".format(rate/n))               #53
                                                         #54
Game()                                                   #55
