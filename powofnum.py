
# 4# POWER OF  NUMBERS
def power(n,e):
    res=1
    for i in range(e):
        res *= n
    return res
print("power of numbers:",power(2,10))