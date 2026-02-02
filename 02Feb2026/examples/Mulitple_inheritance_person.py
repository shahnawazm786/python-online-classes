from single_inheritance import Person

class Athelete:

    def __init__(self, typeofthelete):
        self.athelete=typeofthelete

class Employee(Person,Athelete):
    def __init__(self, fname, lname,typeofethlete,job,salary):
        Person.__init__(self,fname, lname)
        Athelete.__init__(self,typeofethlete)
        self.job=job
        self.salary=salary

    
e=Employee('Rathore','Rahul','Riffle shutter','IT Manager',59000.99)

print(e.fname)
print(e.lname)
print(e.athelete)
print(e.job)
print(e.salary)

