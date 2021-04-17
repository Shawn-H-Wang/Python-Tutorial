TempStr = input("请输入温度值:")
if TempStr[-1] in ['F','f']:
    try:
        Temp = eval(TempStr[0:-1])
    except NameError:
        print("数字格式错误")
    except:
        print("格式错误")
    else:
        C = (Temp - 32) / 1.8
        print("转换后的温度是{:.2f}C".format(C))
    finally:
        print("Program End")
elif TempStr[-1] in ['C','c']:
    try:
        Temp = eval(TempStr[0:-1])
    except NameError:
        print("请按照正确格式输入")
    except:
        print("格式错误")
    else:
        F = Temp * 1.8 + 32
        print("转换后的温度是{:.2f}F".format(F))
    finally:
        print("Program End")
else:
    print("格式错误")
