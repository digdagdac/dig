f=open("example.txt",'r+')
r=open("examplecompress.txt",'w+')
data=f.readlines()
count=1
a=0
for i in data:#
    for j in range(len(i)):
        if(j+1<len(i) and i[j]==i[j+1]):
            count+=1
        elif(count>=5):
            r.write(i[j]+"("+str(count)+")")
            count=1
        else:
            r.write(i[j]*(count))
            count=1
        
