
class Person:
    def __init__(self, name, people_id):
        self.name = name
        self.people_id = people_id

    def greet(self):
        return f"Hello, I'm {self.name} (ID: {self.people_id})"

class Student(Person):
    def __init__(self, name, people_id, email, address, student_id):
        super().__init__(name, people_id)
        self.email = email
        self.address = address
        self.student_id = student_id
    
    def update_email(self, new_email):
        self.email = new_email

    def greet(self):
        return f"Greetings and facilitations from student {self.name} (student ID: {self.student_id})" 

class Lecturer(Person):
    def __init__(self, name, people_id, email, lecturer_id):
        super().__init__(name, people_id)
        self.email = email
        self.lecturer_id = lecturer_id

    def greet(self):
        return f"Greetins from Professor {self.name} (Lecturer ID: {self.lecturer_id})"

def main():
    student = Student("Alice", 101, "alice@example.com", "123 Main St", "S1001")
    lecturer = Lecturer("Dr. Bob", 201, "bob@example.com", "L2001")

    print("Overriding:")
    print("Student greeting:", student.greet())
    print("Lecturer greeting:", lecturer.greet())
   
    person = Person("Charlie", 301)
    print("\nPerson greeting:", person.greet())

    print("\nAdditional:")
    print(f"Student: {student.name}, Email: {student.email}, ID: {student.student_id}")
    print(f"Lecturer: {lecturer.name}, Email: {lecturer.email}, ID: {lecturer.lecturer_id}")


if __name__ == "__main__":
    main()
