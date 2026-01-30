# Base class
class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

# Intermediate class inheriting from the base class
class Employee(Person):
    def __init__(self, name, id, position):
        super().__init__(name, id)
        self.position = position

    def get_position(self):
        return f"Position: {self.position}"

# Another independent base class
class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def get_sport(self):
        return f"Sport: {self.sport}"

# Derived class combining Employee and Athlete
class Student(Employee, Athlete):
    def __init__(self, name, id, position, grade, sport):
        Employee.__init__(self, name, id, position)
        Athlete.__init__(self, sport)
        self.grade = grade

    def get_grade(self):
        return f"Grade: {self.grade}"

# Example usage
student = Student("Samuel", 1234, "Intern", "A", "Soccer")
print(student.get_details())  # From Person
print(student.get_position())  # From Employee
print(student.get_grade())  # From Student
print(student.get_sport())  # From Athlete