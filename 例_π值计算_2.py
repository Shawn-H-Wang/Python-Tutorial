##计算π值
'''
DeprecationWarning: time.clock has been deprecated in
Python 3.3 and will be removed from Python 3.8: use
time.perf_counter or time.process_time instead
'''
from random import random
from math import sqrt
from time import clock
DARTS = 1000 
hits = 0.0
clock()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits/DARTS)
print("圆周率是{}".format(pi))
print("运行时间为{:.5f}".format(clock()))

