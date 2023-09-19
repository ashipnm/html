str1=input("Please enter a string : ")
tot=1
i=0
while(i<len(str1)):
    if(str1[i]==' ' or str1 == '/n' or str1 == '\t'):
        tot=tot+1
    i=i+1
print("Total number of words in the given string= ",tot)
