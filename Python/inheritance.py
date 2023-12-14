class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printName(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x = Student(input('enter the first name: '),input('enter the last name: '))
x.printName()
        
        
        