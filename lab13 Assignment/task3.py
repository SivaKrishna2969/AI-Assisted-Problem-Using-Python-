class Student:
    """
    Represents a student with personal details and academic marks.
    """

    def __init__(self, name, age, marks):
        """
        Initialize a Student object.

        Args:
            name (str): Student's name
            age (int): Student's age
            marks (list of numbers): List of marks in subjects
        """
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        """Print student name and age in a clean format."""
        print(f"\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")

    def total_marks(self):
        """Return sum of all subject marks."""
        return sum(self.marks)


# -------- USER INPUT SECTION --------
name = input("Enter student name: ")
age = int(input("Enter student age: "))

num_subjects = int(input("Enter number of subjects: "))
marks = []

for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Create Student object
student = Student(name, age, marks)

# Display result
student.display_details()
print(f"Total Marks = {student.total_marks()}")
