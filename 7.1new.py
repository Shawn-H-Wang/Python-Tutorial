from keyword import iskeyword
import jieba

def UP(S):
    L = []
    for I in S:
        LX = jieba.lcut(I)
        for X in range(len(LX)):
            print(LX[X])
            if iskeyword(LX[X]) or LX[X] in {'time','turtle','jieba','format',
                                        'sleep','center','range','keyword',
                                        'print','input','eval','int',
                                        'float','double','len','append',
                                        'lcut','iskeyword','upper','writelines',
                                        'open','close'}:
                continue
            else:
                LX[X] = LX[X].upper()
            print(LX[X])
        L.append(LX)
    return L

FILEPATH1 = input("请输入读取文件路径：")
FILEPATH2 = input("请输入修改后文件路径：")
F = open(FILEPATH1 , 'R' , ENCODING = 'UTF-8')
LS = []
LS = UP(F)
F.close()
FN = open(FILEPATH2 , 'W+' , ENCODING = 'UTF-8')
for I in range(len(LS)):
    FN.writelines(LS[I])
FN.close()

