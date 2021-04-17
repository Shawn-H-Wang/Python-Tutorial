a = input("请输入一个字符串:")
x1,x2,x3,x4 = 0,0,0,0
'''
x1-----数字字符个数
x2-----字母字符个数
x3-----空格字符个数
x4-----其他字符个数
'''
for i in a:
    if i == " ":
        x3 += 1
    elif '1' <= i <= '9':
        x1 += 1
    elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        x2 += 1
    else:
        x4 += 1
else:
    print("数字字符个数:{}".format(x1))
    print("字母字符个数:{}".format(x2))
    print("空格字符个数:{}".format(x3))
    print("其他字符个数:{}".format(x4))
