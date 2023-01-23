def passgen2(count):
    
    def passgen1():

        import random as rd
        rand=[]
        list1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        list2=["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        list3=["0","1","2","3","4","5","6","7","8","9"]
        list4=list1+list2+list3
        pwd=list1[rd.randint(0,25)]+list2[rd.randint(0,25)]+list3[rd.randint(0,9)]+list4[rd.randint(0,61)]+list4[rd.randint(0,61)]+list4[rd.randint(0,61)]+list4[rd.randint(0,61)]
        print(pwd)
    for i in range(0,10,1):
        passgen1()
num1=int(input("enter number of passwords required: "))
passgen2(num1)
