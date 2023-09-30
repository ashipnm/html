#input:232
#output:17
n=(input("enter a number:"))
def sl(): 
    sum=0
    for i in n:
        sum+=(int(i)**2)
    print(sum)
sl()