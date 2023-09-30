#first list[1,2,3,4]
#second list [2,2,5,6,4]
#output:[2,4]
fl=[1,2,3,4]
f2=[2,2,5,6,4]
def cm():
    f3=[]
    s1=set(fl)
    s2=set(f2)
    f3=s1.intersection(s2)
    print(list(f3))          
cm()
       
