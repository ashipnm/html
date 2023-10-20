
# 2#Remove duplicated from sorted array
def sort(list):
    list1=[]
    for i in list:
        if i not in list1:
            list1.append(i)

    return  list1
list=list(input("enter a list:"))
print("Sorted list are after removing duplicates:",sort(list))