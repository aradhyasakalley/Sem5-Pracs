# Classes and Objects:
class MyClass:
    a = 10
p1 = MyClass()
print(p1.a)

# Use of __init__() function in class:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Object Methods, Modification of Object Properties, Deleting Object Properties and Objects:
class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    def printName(self):
        print(self.firstname, self.lastname)
p1 = Person(input("Enter first name: "), input("Enter last name: "), input("Enter age: "))
p1.printName()
p1.firstname = "Anuj"
p1.printName()
print("Age is:", p1.age)
del p1.age # deleting object property
del p1 # deleting object

# Python Inheritance:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printName(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self, fname, lname):
    # Person.__init__(self, fname, lname)
        super().__init__(fname, lname) # Here self isn't required
x = Student(input("Enter first name: "), input("Enter last name: "))
x.printName()

