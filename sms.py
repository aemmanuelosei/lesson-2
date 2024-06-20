from sms_program import *
print("*welcome to kojo's student management system*")
while True:
    menu_display()
    option = int(input("please make a selection from the following options: \n"))
    print(option)
    if option == 1:
        define_student()
    elif option == 2:
        view_records()
    elif option == 3:
        update_records()
    elif option == 4:
        delete_records()
    elif option == 5:
        exit()
    else:
        print("wrong entry, please select from 1 - 5")