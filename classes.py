students = []


class Student:

    school_name = "My School"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalized(self):
        return self.name.capitalize()


    def get_schoolName(self):
        return self.school_name


#mark = Student("Mark")
#print(mark)

print(Student.school_name)

