class Student:
    def __init__(self, name, roll_number, subject_marks, total_marks):
        self.name = name
        self.roll_number = roll_number
        self.subject_marks = subject_marks
        self.total_marks = total_marks

    def calculate_percentage(self):
        total_obtained_marks = sum(self.subject_marks.values())
        return (total_obtained_marks / self.total_marks) * 100

    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return 'A'
        elif 80 <= percentage < 90:
            return 'B'
        elif 70 <= percentage < 80:
            return 'C'
        elif 60 <= percentage < 70:
            return 'D'
        else:
            return 'F'

    def print_marksheet(self):
        print("\nStudent Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Subjects and Marks:")
        for subject, marks in self.subject_marks.items():
            print(f"{subject}: {marks}")
        print("Total Marks:", self.total_marks)
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.calculate_grade())

# Example usage:
if __name__ == "__main__":
    # Create a student object
    student1 = Student("John Doe", "2023001", {"Math": 91, "English": 91, "Science": 77, "History": 88}, 400)

    # Print the mark sheet
    student1.print_marksheet()

    student2 = Student("Om", "2023001", {"Math": 85, "English": 92, "Science": 78, "History": 95, "Art": 88}, 500)

    # Print the mark sheet
    student2.print_marksheet()
