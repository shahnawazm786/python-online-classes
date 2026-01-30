class Person:
    def get_details(self):
        return "Details of a person."

class Athlete:
    def get_skill(self):
        return "Athletic skills."

class Student(Person, Athlete):
    pass

# Example usage
student = Student()
print(student.get_details())
print(student.get_skill())

print(Student.__mro__)