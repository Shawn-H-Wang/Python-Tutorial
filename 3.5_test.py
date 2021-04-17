str1='+'
str2='/'
for i in range(11):
    if i % 5 in [0]:
        print("{}{}{}".format(str1,str1.center(9,'-'),str1))
    else:
        print("{}{:>5}{:>5}".format(str2,str2,str2))
