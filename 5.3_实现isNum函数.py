def isNum(x):
    n = type(eval(x))
    if n == int:
        return True
    elif n == float:
        return True
    else:
        return False

def main():
    s = input("请输入一个字符串：")
    print(isNum(s))

main()

'''
????????????????
'''
