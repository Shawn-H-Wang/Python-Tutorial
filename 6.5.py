import random

def Same():
    dic= {}
    c = 0
    count = 0
    counts = 0
    time = pow(2,15)
    people = 23
    for cx in range(time):
        while c <= time:
            for i in range(people):
                dic[i] = random.randint(1,366)
            if isSame1(dic,people):
                count += 1
            c += 1
        counts += count
    print("其中至少两个人在同一天过生日的概率为：{:.2f}%".format(counts/pow(time,2)*100))
##    print(dic.items())
##    for i in range(23):
##        dic[i] = random.randint(1,366)
##    isSame1(dic)
    
def isSame1(d,man):
    lx = []
    x = False
    for i in range(man):
        lx.append(d[i])
    lx = set(lx)
    if len(lx) != man:
        x = True
##    print(lx)
##    print(len(lx))
    return x

Same()
