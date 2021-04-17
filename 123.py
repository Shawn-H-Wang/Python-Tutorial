f1 = open('6.5.txt' , 'r' , encoding = 'utf-8')
##line = f1.readline()

##for line in f1.readlines():
##for line in f1:
##    print(line)

##f1.seek(2)
##f1.writelines(['abc\n','def','\nghijk'])
##f1.seek(0)
##f1.write('nihao\nshijie')
##for lines in f1.readlines():
##    print(lines)

lines = f1.readlines()
print(lines)
f1.close()
