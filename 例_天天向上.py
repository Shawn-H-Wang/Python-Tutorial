dayup=1.0
dayfactor=0.01
for i in range(365):
    if i % 7 in [6, 5]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("向上5天，向下2天的力量:{:.2f}.".format(dayup))
