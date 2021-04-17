def ff():
    fo = open("1.csv","r")
    ls = []
    for line in fo:
        line = line.replace("\n","")
        ls.append(line.split(","))
    print(ls)
    fo.close()

def ffx():
    fo = open("1.csv","r")
    ls = []
    for line in fo:
        line = line.replace("\n","")
        ls = line.split(",")
        lns = ""
        for i in ls:
            lns += "{}\t".format(i)
        print(lns)
    fo.close()

def fw():
    fr = open("1.csv","r")
    fw = open("1new","w")
    ls = []
    for line in fr:
        line = line.replace("\n","")
        ls.append(line.split(","))
    for i in ls:
        for j in i:
            if j.replace(".","").isnumeric():
                j = "{:.2}%".format(float(j)/100)
    for row in ls:
        print(row)
        fw.write(",".join(row)+"\n")
    fr.close()
    fw.close()

fw()
##ff()
##print("*"*80)
##ffx()
