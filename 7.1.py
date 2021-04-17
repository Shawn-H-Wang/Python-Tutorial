from keyword import iskeyword
import jieba

def up(s):
    l = []
    for i in s:
        lx = jieba.lcut(i)
        for x in range(len(lx)):
            if lx[x] is '\n':
                continue
            print(lx[x])
            if iskeyword(lx[x]) or lx[x] in {'time','turtle','jieba','format',
                                        'sleep','center','range','keyword',
                                        'print','input','eval','int',
                                        'float','double','len','append',
                                        'lcut','iskeyword','upper','writelines',
                                        'open','close'}:
                continue
            else:
                lx[x] = lx[x].upper()
            print(lx[x])
        l.append(lx)
    return l

filePath1 = input("请输入读取文件路径：")
filePath2 = input("请输入修改后文件路径：")
f = open(filePath1 , 'r' , encoding = 'utf-8')
ls = []
ls = up(f)
f.close()
fn = open(filePath2 , 'w+' , encoding = 'utf-8')
for i in range(len(ls)):
    fn.writelines(ls[i])
fn.close()

