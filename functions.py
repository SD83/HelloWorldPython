#def var_args(name,*args):
#   print(name)
#    print(args)


#def var_args1(name, **kwargs):
    #    print(name)
#   print(kwargs["description"], kwargs["feedback"])


#var_args1("Mark", description="Loves python", feedback=None, pluralsight_subscriber=True)

students = []


def get_student_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_student_titlecase()
    print(students_titlecase)


def add_student(name,student_id=332):
    student = {"name": name,"student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt","a")
        f.write(student+"\n")
        f.close()
    except Exception:
        print("Can not save file")


def read_file():
    try:
        f = open("students.txt","r")
        for student in f.readlines():
            add_student(student)
        f.close()

    except Exception:
        print("Can not read file")


#student_list = get_student_titlecase()
read_file()
print_student_titlecase()

student_name = input("Enter Student Name :")
student_id = input("Enter Student Id :")

add_student(student_name,student_id)
save_file(student_name)



