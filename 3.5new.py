import time
STR1='+'
STR2='|'
for I in range(11):
    if I % 5 in [0]:
        print("{}{}{}".format(STR1,STR1.CENTER(9,'—'),STR1))
    else:
        print("{}{:>9}{:>9}".format(STR2,STR2,STR2))
    time.SLEEP(0.1)
