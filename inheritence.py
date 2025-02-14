#this is where the child class inherits the properties of a parent class
class parent_class:
    #body of parent class
    pass
class child_class(parent_class):#nherits
    #body of child class
    pass

class Human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def info(self):
        print(f"Hey my name is {self.name}, I'm {self.gender}, and I'm {self.age} years old")
    
class Boy(Human):
    def school(self, schoolname):
        print(f"i study in {schoolname}")
        pass
        
b = Boy("james", 15, "male")
b.info()
b.school("UTAMU")
pass
        
        #the super class
        
class Boy(Human):
    def __init__(self,name,age,gender,schoolname):
        super().__init__(name,age,gender)
        self.schoolname=schoolname
        
    def school(self):
        print(f"i study from{self.schoolname}")
        

b = Boy("james", 15, "male", "UTAMU")
b.info()
b.school()

    