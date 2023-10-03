#prime numbers in series 
n=int(input("enter the low range :"))
m=int(input("enter the high range:"))
def prime(x,y):
    print("prime number range are:")
    for i in range(x,y+1):
        if i>1:  
             for j in range (2, i):  
                 if (i % j) == 0:  
                      break  
             else: 
                  print (i)  
           
print(prime(n,m))         
