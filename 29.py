def assigncode(name1):
    name=name1
    start1=65
    start2=97
    size1=26
    upper=[]
    lower=[]
    special=[" "]
    num1=[]
    num2=[]
    codename=[]
    codenumber=0
    for i in range(0,size1,1):
        upper.append(chr(start1+i))
        lower.append(chr(start2+i))
        num1.append(start1+i)
        num2.append(start2+i)      
    len1=len(name)
    for i in range(0,len1,1):
        
        try:
            pos1=upper.index(name[i])
        except:
            try:
                pos1=lower.index(name[i])+size1
            except:
                pos1=special.index(name[i])+2*size1
        codename.append(str(pos1).zfill(2))
    codenumber="".join(codename)
    print("Dear "+name+", your codename is "+codenumber+". Happy Birthday ")
assigncode("NN")
