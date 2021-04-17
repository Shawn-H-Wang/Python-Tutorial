fileread=input("Please input the read-filePath:")
fo = open(fileread,"r",encoding="utf-8")
filewrite=input("Please input the write-filePath:")
fi = open(filewrite,"a",encoding="utf-8")
ls = fo.readlines()
count=0
m=0
for i in range(len(ls)):
    if m < len(ls[i]):
        m=len(ls[i])
for i in range(len(ls)):
    count += 1
    ls[i]=ls[i].replace("\n","")
    ls[i] += (m-len(ls[i]))*" "
    ls[i]=ls[i]+"#"+str(count)+"\n"
for i in ls:
    fi.write(i)
fo.close()
fi.close()
print("File has been written successfully!!")
