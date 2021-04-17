while[1 == 1]:
    MONEY = input("请输入一种金钱数:")
    if MONEY[0] in ['$']:
        if MONEY[1] in ['1','2','3','4','5','6','7','8','9']:
            RMB = eval(MONEY[1:])*6
            print("转换过后的钱是RMB:{:.2F}".format(RMB))
        else:
            print("ERROR")
    elif MONEY[0] in ['R','R']:
        if MONEY[1] in ['1','2','3','4','5','6','7','8','9']:
             DOL = eval(MONEY[1:])/6
             print("转换过后的钱是$:{:.2F}".format(DOL))
        else:
            print("ERROR")
    else:
        print("ERROR")
        break
