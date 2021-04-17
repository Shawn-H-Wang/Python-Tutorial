import random
# 新建列表类型存储字符串和数字
strs = []
# 添加字符
for i in (65,97):
    for j in range(26):
        strs += chr(i+j)
# 添加数字
for i in range(10):
    strs += str(i)
# 输出10个8位的密码
for i in range(10):
    print("密码", i+1, ":",end= '')
    for j in range(8):
        print(strs[random.randint(0,61)], end= '')
    print()
