def menu_display():
    print("1.select 1 to register student\n")
    print("2.select 2 to view student records\n")
    print("3.select 3 to update student records\n")
    print("4.select 4 to delete student records\n")
    print("5.select 5 to exit program\n")

def records(start, student_id, name, age, gender, course):
    start.student_id = student_id
    start.name = name
    start.age = age
    start.gender = gender
    start.course


    start.students = []

def register_student(start):
    student_id = int(input("Please type student ID: \n"))
    name = input("Please type student name: \n")
    age = int(input("Please type student age: \n"))
    gender = input("Please enter student gender: \n")
    course = input("Please enter student course: \n")
    student = student(student_id, name, age, gender, course)
    start.students.append(student)
    print("Student registered successfully")

def view_student(start, student_id):
    for student in start.students:
        if student.student_id == student_id:
            print(f"Student ID: {student.student_id}")
            print(f"Name:{student.name}")
            print(f"Age:{student.age}")
            print(f"Gender:{student.gender}")
            print(f"Course:{student.course}")
            return
        print("Student records not found")

def update_student(start, student_id):
    for student in start.students:
        print("Please enter new records: \n")
        name = input(f"Please enter new name(new:{student.name}): \n")
        age = int(input(f"Please enter new age(new:{student.age}): \n"))
        gender = input(f"please enter new gender(new:{student.gender})")
        course = input(f"Please enter new course(new:{student.course})")
        print("Student records updated successfully")
        return
    else:
        print("Student records not found")

def delete_student(start, student_id):
    for student in start.students:
        if student.student_id == student_id:
            start.students.remove(student)
            print("Student records deleted successfully")