while[1 == 1]:
    money = input("请输入一种金钱数:")
    if money[0] in ['$']:
        if money[1] in ['1','2','3','4','5','6','7','8','9']:
            Rmb = eval(money[1:])*6
            print("转换过后的钱是RMB:{:.2f}".format(Rmb))
        else:
            print("error")
    elif money[0] in ['r','R']:
        if money[1] in ['1','2','3','4','5','6','7','8','9']:
             Dol = eval(money[1:])/6
             print("转换过后的钱是$:{:.2f}".format(Dol))
        else:
            print("error")
    else:
        print("error")
        break
