import time
str1='+'
str2='|'
for i in range(11):
    if i % 5 in [0]:
        print("{}{}{}".format(str1,str1.center(9,'—'),str1))
    else:
        print("{}{:>9}{:>9}".format(str2,str2,str2))
    time.sleep(0.1)
