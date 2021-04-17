i = input("请输入一个五位数:")
x = i[::-1]
if i == x:
    print("这个数是一个回文数")
else:
    print("这个数不是一个回文数")
