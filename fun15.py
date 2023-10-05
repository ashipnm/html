#write a python program to find and print all the pairs of numbers whose product is even and sum is odd 
list=[2,3,4,5,6]
oddlist=0
evelist=0
def oesum(list,oddlist,evelist):
    print("list is :",list)
    for i in list:
        for j in str(i):
            if int(j)% 2==0:
                evelist += int(j)
            else :
                oddlist += int(j)
    print("odd sum=",oddlist)
    print("even sum=",evelist)
oesum(list,oddlist,evelist)                
       