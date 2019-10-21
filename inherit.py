
class Student():
    def __init__(self,student_nam):
        self.student_nam = student_nam

    def get_name(self):
        print (f"Student name is {self.student_nam}")

class Teacher(Student):
    def __init__(self,student_name,teacher_name,teaching_subjects,salary):
        super().__init__(student_name)
        self.teacher_name = teacher_name
        self.teaching_subjects =  teaching_subjects
        self.salary = salary

    def print_teacher(self):
        print (f"{self.student_nam} is taught by {self.teacher_name}")

student1= Student("Gita")
student1.get_name()
teacher1= Teacher("Git","Binita Sharma","science",20000)

teacher1.print_teacher()