l=[]
def create():
    n=int(input("enter no of elements:"))
    for i in range(n):
        p=int(input("enter:"))
        l.append(p)
    print(l)
def add():
    print("add new items in list:")
    m=int(input("enter new item:"))
    l.append(m)
    print(l)
def replace():
    print("replace the list ")
    q=int(input("replace the item:"))
    l.pop(2)
    l.insert(2,6)
    print(l)       
def remove():
    print("remove items in a list: ")
    o=int(input("remove item:"))
    l.remove(o)
    print(l)
def sort():
    print("sort the liste are:")
    l.sort()  
    print(l)   
while True:
    choice=int(input("enter the choice:"))
    if choice==1:
        create()
    if choice==2:
        add()
    if choice==3:
        replace()     
    if choice==4:
        remove()
    if choice==5:
            sort()
    if choice==6: 
        print("exit")
        break        