list1=[90,95,100]
len1=len(list1)
mean=sum(list1)/len1
meansquared=sum((x-mean)**2 for x in list1)
variance=meansquared/len1
print(variance)

