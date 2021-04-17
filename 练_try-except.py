try:
    num = eval(input("Please input a intager number:"))
    print(num**2)
except NameError:
    print("Name Error")
except:
    print("Other Error")
#try中无错误是进行
else:
    print("No Exception")
#无论是否有错误，最终都要进行
finally:
    print("Program End")
