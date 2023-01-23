import datetime
today = datetime.datetime.now()
print(today)
f1=open("audit","w")
for j in range(3,8,1):
    
    for i in range(1,11,1):
        info=str(j) +"*"+str(i) +"="+str(j*i)
        print(info)
        f1.write(info)
        f1.write("\n")
    print()
    f1.write("\n")
f1.close()
