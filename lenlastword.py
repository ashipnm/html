5#LENGTH OF A LAST WORD
def length(l):
    words=l.split()
    if len(words)==0:
        return 0
    return len(words[-1])
n=input("enter a word:")
print(length(n))