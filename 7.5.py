d = {}
while True:
    cho = input("请输入选择功能：1-添加 2-查询 3-退出：")
    if cho is "1":
        f = open("dictionary.txt","w")
        word = input("请输入添加的单词：")
        mean = input("请输入添加单词的意思：")
        lw = [word , mean]
        f.writelines(lw)
    elif cho is "2":
        f = open("dictionary.txt","r")
        ls = []
        for line in f:
            line = line.replace("\n","")
            ls.append(line.split(":"))
        f.close()
    elif cho is "3":
        print("退出程序！")
        break
    else:
        print("输入错误，请重新输入！")
        continue


def main():
    pro = input("请输入选择功能：1-添加 2-查询 3-退出：")
    while True:
        if pro is "1":
            add()
        elif pro is "2":
            serch()
        elif pro is "3":
            esc()
            break
        else:
