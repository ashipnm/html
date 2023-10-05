#convert decimal number to binery,octal and hexa decimal
n=int(input("enter a decimal value:"))
def con(n):
 print('the  binery of the number  ',n,'is' ,bin(n))
 print('The octal of the number ',n,'is',oct(n))
 print('The hexa decimal of the number ',n,'is',hex(n))
print(con(n))

