#*
#1
#**
#12
#***
#321
#****
#1234
#*****
#12345
n=int(input("enter a rows:"))
def pyramid(n):
   for i in range(1,n+1):
    for j in range(0,i):
      print("*",end="")
    print()
    if i % 2==0:
      for j in range(1,i+1):
        print(j,end='')
    else:
      for j in range(i,0,-1):
         print(j,end='')
    print()    
pyramid(n)         