##每15天休息一次的周期学习
year=365
dayup=1.0
for i in range(year+1):
    if i==0:
        continue
    if i % 15 in [4,5,6,7,11,12,13,14]:
        dayup *= (1 + 0.01)
    else:
        dayup = dayup
print("365天后的学习能力值为:{:.6f}".format(dayup))
