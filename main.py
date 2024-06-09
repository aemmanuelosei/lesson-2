# import our program module
from program import *
# welcome message
print("***kojo Blood's to-do list application***")
# get user input

while True:
    # invocation of the menu function
    display_menu()
    # accepting user option
    user_option = int(input("Kindly choose from the following options\n"))
    # check if user option is 1
    if user_option == 1:
        add_tasks()
    elif user_option == 2:
        view_tasks()
    elif user_option == 3:
        update()
    elif user_option == 4:
        delete()
    elif user_option == 5:
        exit()
    else:
        print("Invalid option. kindly choose an option between 1 - 5")