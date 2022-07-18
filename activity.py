class Student(object):
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def selfGrade(self):
        return self.grade

Dylan=Student("Dylan",15,10)
Roblox=Student("Roblox",16,12)
print(Dylan.age)

class Company(object):
    def __init__(self,flavor,color):
        self.flavor=flavor
        self.color=color

McDonalds=Company("Cheeseburger","yellow")