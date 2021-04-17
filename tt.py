fileread=input("Please input the read-filePath:")   #1
fo = open(fileread,"r",encoding="utf-8")            #2
filewrite=input("Please input the write-filePath:") #3
fi = open(filewrite,"a",encoding="utf-8")           #4
ls = fo.readlines()                                 #5
count=0                                             #6
m=0                                                 #7
for i in range(len(ls)):                            #8
    if m < len(ls[i]):                              #9
        m=len(ls[i])                                #10
for i in range(len(ls)):                            #11
    count += 1                                      #12
    ls[i]=ls[i].replace("\n","")                    #13
    ls[i] += (m-len(ls[i]))*" "                     #14
    ls[i]=ls[i]+"#"+str(count)+"\n"                 #15
for i in ls:                                        #16
    fi.write(i)                                     #17
fo.close()                                          #18
fi.close()                                          #19
print("File has been written successfully!!")       #20
