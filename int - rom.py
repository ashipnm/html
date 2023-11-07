1#CONVERT INTEGER TO ROMAN
def solve(num):
   res = ""
   table = [
      (1000, "M"),
      (500, "D"),
      (100, "C"),
      (50, "L"),
      (10, "X"),
      (5, "V"),
      (1, "I"),
   ]
   for cap, roman in table:
      d, m = divmod(num, cap)
      res += roman * d
      num = m

   return res

num =int(input("enter a number to convert a roman:"))
print("Roman letters are:",solve(num))

