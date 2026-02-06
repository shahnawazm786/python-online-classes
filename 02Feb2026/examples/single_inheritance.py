# Inheritance 
# Parent Class and Child class
# Parent class properties and method inherited into the children class
# Single inheritance Parent class -> Child class
# car is a Viechles
class Person:
    
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    
class Student(Person):

    def __init__(self, fname, lname,standard): # define method
        super().__init__(fname, lname) # super() method 
        self.standard=standard # child class 

    def get_info(self):
        print(f'First name = {self.fname} Last name = {self.lname} and Studied in {self.standard}')


# p=Person('Rahman','Abdul')
# print(p.fname)
# print(p.lname)

s=Student('Rahman','Abdul','B.Tech')
s.get_info()
