##定义一个函数用来计算工作5天，休息2天的效果
def dayUP(dayFactor):
    dayup = 1.0
    for i in range(365):
        if i & 7 in [0, 6]:
            dayup *= (1 - 0.01)
        else:
            dayup *= (1 + dayFactor)
    return dayup

dayfactor=0.01
Dayup = 1.0

for i in range(365):
    Dayup *= (1+0.01)
while (dayUP(dayfactor)<Dayup):
    dayfactor += 0.001
print("每天的努力参数是:{:.3f}.".format(dayfactor))
