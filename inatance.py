class Human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
        #x and y are Instancesof a class Human
x = Human("alex", 24, "male")
y = Human("grace", 23, 'female')

print(x.name)
print(y.name)