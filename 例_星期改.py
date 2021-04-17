weekstr="一二三四五六七"
weekid=eval(input("请输入星期数字(1-7):"))
pos=weekid-1
print("星期{}".format(weekstr[pos:pos+1]))
