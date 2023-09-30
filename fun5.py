#print square rach list using for loop
#input[2,5,8,9,7]
#output[4,25,64,81,49]
num=[2,5,8,9,7]
def sq(num):
    print(num)
    s=[]
    for i in num:
        s.append(i*i)
    print("output will be",s)        
sq(num)