dayup = 1.0
for i in range(365+1):
    if i==0:
        continue
    if i % 7 in [1,2,3]:
        dayup = dayup
    else:
        dayup = dayup * (1 + 0.01)
print("365天后的学习能力值为:{:.6f}".format(dayup))
