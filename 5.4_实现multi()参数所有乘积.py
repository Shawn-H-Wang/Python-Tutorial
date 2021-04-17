def multi(a):
    if a >= 10:
        x = a%10
        return x*multi((int)(a/10))
    else:
        return a

def main():
    num = eval(input("请输入一段参数："))
    al = multi(num)
    print("各项参数的乘积为：{}".format(al))

main()
