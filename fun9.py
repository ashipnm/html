#print fibanacci series
def fibonacci(n):
  a=0
  b=1
  fib= []
  for i in range(n):
    fib.append(a)
    a=b
    b=a+b
  return fib
print("fibonacci series of ",fibonacci(5))