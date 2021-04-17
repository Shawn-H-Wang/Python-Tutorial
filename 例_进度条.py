import time
scale = 10
print("strat".center(28,'-'))
for i in range(scale+1):
    a, b='**'*i, '..'*(scale-i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.5)
print("end".center(28,'-'))
