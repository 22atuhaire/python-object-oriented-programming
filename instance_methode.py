class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        #instance method
    def speak(self):
        return f"hello everyone! i'm {self.name}"
    def eat(self, favouriteDish):
        return f"i love to eat {favouriteDish}!!!"
    
x = Human("john", 24, "male")
print(x.age)
print(x.speak())
print(x.eat("mangoes"))