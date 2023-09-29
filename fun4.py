# string is:"abcd@#$$%^&efg"
# output will be:"abcdefg"
n="ashi!@#$pnm"
def name(n): 
    m=''    
    for i in n:
        if(i.isalpha()):
            m+=i
    print(m)
name(n)
