def isOdd(x):
    if isNum(x):
        for i in x:
            if i == '.':
                print("这个数不是一个正整数！！")
                break
        else:
            a = (int)(x)
            if a == 1:
                print("这个数为奇数！")
            elif a%2 == 0:
                print("这个数为偶数！")
            else:
                print("这个数为奇数！")
    else:
        print("这个数不是一个正整数！！")

def isNum(s):
    for ch in s:
        if s < '0' or s > '9':
            print("这个数不是一个正整数！！")
            return False
            break
    else:
        return True

isOdd("1.2")
isOdd("35")
isOdd("12")
isOdd("-51")
isOdd("abc")
