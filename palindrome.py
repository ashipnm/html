str_1 = input("Enter the string to check if it is a palindrome:" )
str_1 = str_1.casefold ()
rev_str = reversed (str_1)
if list (str_1) == list (rev_str):
              print (str_1," is a palindrome.")
else:
              print (str_1,"is not a palindrome.")
              #output
#check whether enter word is palindrome or not
#Enter the string to check if it is a palindrome:malayalam
#malayalam is a palindrome