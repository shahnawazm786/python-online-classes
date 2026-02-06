class Student:

    def __init__(self,roll,name,grade,marks):
        self.roll=roll
        self.name=name
        self.__grade=grade # __variablename (private)
        self._marks=marks # _variablename protected
    
    def get_info(self): #public
        print('Roll no',self.roll)
        print('Name',self.name)
        print('Marks',self._marks)
        print('Grade',self.__grade)

s=Student(1,'Abdullah','A',655)
print('Calling the public method where private variable is called')
s.get_info() #public method 
print('Trying to access class properties  outside scope')
print(s.roll) #public
print(s.name) #public
print(s._marks) # protected 
print('__grade is private variable and we are trying call outside scope')
print(s.__grade) #error becuase it is private variables

