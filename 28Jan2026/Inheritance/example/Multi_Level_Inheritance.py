class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(Person):
    def __init__(self, name, id, grade):
        super().__init__(name, id)
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}"

class GraduateStudent(Student):
    def __init__(self, name, id, grade, thesis_title):
        super().__init__(name, id, grade)
        self.thesis_title = thesis_title

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}, Thesis: {self.thesis_title}"

# Example usage
grad_student = GraduateStudent("Charlie", 91011, "A", "AI in Healthcare")
print(grad_student.get_details())