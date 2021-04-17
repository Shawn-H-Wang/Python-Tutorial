def isTrue(s):
    x = set(s)
    if len(x) == len(s):
        print(True)
    else:
        print(False)

x=input("请输入一个字符串：")
isTrue(x)
