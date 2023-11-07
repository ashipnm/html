class animal:
    def __init__(self,sound): 
      self.sound=sound
# Parent Class 
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

# Child Class 1
class Dog(Animal):
    def sound(self):
        return "Bark!"

# Child Class 2
class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Mittens")
print(dog.name)  
print(dog.sound())  
print(cat.name) 
print(cat.sound())    