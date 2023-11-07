class Temprature:
    def __init__(self,t):
        self.temprature=t
    def celsius(self):
        return self.fahrenheit*1.8+32
    def fahrenheit(self):
        return self.celsius*1.8+32    
T=Temprature(5)
print(T.celsius())
print(T.fahrenheit())    