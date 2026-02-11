from single_inheritance import Person

class Employee(Person):

    def __init__(self, fname, lname,empid,salary):
        super().__init__(fname, lname)
        self.empid=empid
        self.salary=salary

    def get_info(self):
        print('🚨 Employee Details 🚨')
        print(f'\n🚨 Employee id {self.empid}')
        print(f'\n🚨 First name {self.fname}')
        print(f'\n🚨 Last name {self.lname}')
        print(f'\n🚨 Salary {self.salary}')

e1=Employee('Rahman','Abdul',1001,45000.99)
e1.get_info()
