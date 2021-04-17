def isTrue(ls):
    for i in range(len(ls)):
        x = ls[i]
        del ls[i]
        if isChong(ls,x):
            print(True)
            break
        ls.insert(i,x)
    else:
        print(False)

def isChong(ls,chx):
    x = False
    for j in range(len(ls)):
        if ls[j] == chx:
            x = True
            break
    else:
        x = False
    return x

def main():
    l = []
    while True:
        ch = input("请输入本次需要增加的元素：")
        l.append(ch)
        if ch == "":
            break
    isTrue(l)

main()
