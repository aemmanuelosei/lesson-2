# registereing a new student
student_records = {}

def define_student():
  
            # student_records[student_id] = {"name": name, "age": age, "gender": gender, "course": course}
            student_id = int(input("Please enter student ID: \n"))
            name = input("Please enter student name: \n").capitalize()
            age = int(input("Please enter student age: \n"))
            gender = input("Please enter student gender: \n").capitalize()
            course = input("please enter student course: \n").capitalize()
            print(f"student records {student_id} successfully created")

# viewing student records
def view_records():
    student_id = int(input("please enter student ID to view: \n"))
    for student_id in student_records:
        if student_id in student_records:
            print("student ID:", student_id)
            print("name:", student_records[student_id]["name"])
            print("age:", student_records[student_id]["age"])
            print("gender:", student_records[student_id]["gender"])
            print("course:", student_records[student_id]["course"])
    else:
        for i, student_id in enumerate(student_records, 1):
               print(f"{i}. {student_id}")

# menu display
def menu_display():
    print("1.select 1 to register student\n")
    print("2.select 2 to view student records\n")
    print("3.select 3 to update student records\n")
    print("4.select 4 to delete student records\n")
    print("5.select 5 to exit program\n")


# updating student records
def update_records():
    print("Please find the available records below")
    view_records
    student_id = int(input("enter student ID for update: \n"))
    if student_id in student_records:
        name = input("please enter new name for update: \n").capitalize()
        age = int(input("please enter new age for update: \n"))
        gender = input("please enter gender for update: \n").capitalize()
        course = input("please enter course for update: \n").capitalize()
        if name:
            student_records[student_id]["name"] = name
        if age:
            student_records[student_id]["age"] = age
        if gender:
            student_records[student_id]["gender"] = gender
        if course:
            student_records[student_id]["course"] = course
        print("student records successfully updated")
    else:
        print("student records cannot be found")

# deleting student records
def delete_records():
    student_id = input("please enter student ID for deletion: \n")
    if student_id in student_records:
        delete_records = student_records.pop(student_id - 1)
        print(f"student records '{delete_records}' successfully deleted")
    else:
        print(f"student records cannot be found")

# exiting app
def exit_app():
    exit