#创建列表
def makeLs():
    ls = []
    for i in range(128):
        ls += chr(i)
    return ls

#寻找最长行
def maxLs(ls):
    m = 0
    for i in range(len(ls)):
        Rlength = actL(ls[i])
        if m <= Rlength:
            m = Rlength
    return m

#每一行的实际长度
def actL(s):
    l = len(s)
    ls = makeLs()
    for c in s:
        if not c in ls:
            l += 1
    return l

#重写列表元素
def allnew(ls):
    lw = []
    count = 0
    m = maxLs(ls)
    for line in ls:
        count += 1
        line = line.replace("\n","")
        ll = actL(line)
        line += " "*(m-ll)
        line += "#"+str(count)+"\n"
        lw += line
    return lw
    
#开始读写程序
def bianhao():
    fr = open("30-1828070097-王赫-数据科学编程基础-作业4.py",
              "r",encoding = "utf-8")
    fw = open("30-1828070097-王赫-数据科学编程基础-作业4_new.py",
              "a",encoding="utf-8")
    ls = fr.readlines()
    lw = allnew(ls)
    for lin in lw:
        fw.write(lin)
    fr.close()
    fw.close()
    print("程序结束！！")

bianhao()
