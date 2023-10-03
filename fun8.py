#factorial of a number
n=int(input("enter a number:"))
def fact():
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial is",f)  
fact()        
