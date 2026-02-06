class Student:

    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self._marks=marks # _variablename protected
    
    def get_info(self): #public
        print('Roll no',self.roll)
        print('Name',self.name)
        print('Marks',self._marks)
        self.__grade_calculation()
        print('Marks',self.__grade)
        
            
    def __grade_calculation(self):
        if self._marks >650 :
            self.__grade='A'
        elif self._marks <=650 and self._marks >500 :
            self.__grade='B'
        elif self._marks <=500 and self._marks >400 :
            self.__grade='C'
        elif self._marks <=400 and self._marks >300 :
            self.__grade='D'
        else:
            self.__grade='Bad'

    def __str__(self):
        return f'Studnet information \n Roll no => {self.roll} \n Name => {self.name} \n Marks =>{self._marks} \n Grade =>{self.__grade}'

    
s=Student(1,'Abdullah',655)
print('Calling the public method where private variable is called')
s.get_info() #public method 
print('Calling directly to private method')
#s.__grade_calculation() #private method
print(s)




