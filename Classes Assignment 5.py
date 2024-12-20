class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} has been enrolled in {self.name}.")

    def display_info(self):
        print(f"School Name: {self.name}")
        print(f"Address: {self.address}")
        print("Students Enrolled:", ", ".join(self.students))


class HighSchool(School):
    def __init__(self, name, address, principal):
        super().__init__(name, address)
        self.principal = principal

    def display_info(self):
        super().display_info()
        print(f"Principal: {self.principal}")


school = School("Greenwood Elementary", "123 Maple Street")
high_school = HighSchool("Lincoln High School", "456 Oak Avenue", "Mr. Johnson")


school.enroll_student("Alice")
school.enroll_student("Bob")

high_school.enroll_student("Charlie")
high_school.enroll_student("Daisy")


print("\nElementary School Info:")
school.display_info()

print("\nHigh School Info:")
high_school.display_info()
