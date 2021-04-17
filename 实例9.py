#获得数据
def getNum():
    nums = []
    iNumStr = input("请输入数字(按回车换行结束)：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字(按回车换行结束)：")
    return nums

#计算平均值
def mean(numbers):
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

#计算标准差
def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean) ** 2
    return pow(sdev / (len(numbers) - 1) , 0.5)

#计算中位数
def median(numbers):
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size//2-1] + new[size//2]) / 2
    else:
        med = new[size//2]
    return med
n = getNum()
m = mean(n)
print("平均值：{}，标准差：{:.2}，\
      中位数：{}.".format(m,dev(n,m),median(n)))
