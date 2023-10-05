#implement a function the sorts a list of numbers in ascending or descending order according to the user input
list=list(input("enter a list:"))
x=[]
def descsort(list):
    x=sorted(list)
    print("Sorted list is:",x)
descsort(list)    