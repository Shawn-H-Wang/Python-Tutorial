str1=input("请输入你现在的质量:")
weight=eval(str1[0:-2])
print("你现在在地球上的体重是:{:.3f}N".format(weight*10))
print("你现在在月球上的体重是:{:.3f}N".format(weight*10*0.165))
print("你现在在地球和月球上的质量都一样为:{:.2f}Kg".format(weight))
year=10
for i in range(year):
    weight += 0.05
print("十年后你在地球上的体重是:{:.3f}N".format(weight*10))
print("十年后你在月球上的体重是:{:.3f}N".format(weight*10*0.165))
print("十年后你在地球和月球上的质量都一样为:{:.2f}Kg".format(weight))
