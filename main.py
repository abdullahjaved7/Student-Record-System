from students import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    top_student,
    average_grades,
)


from storage import save_data, load_data

from helpers import get_integer

students = []

load_data(students)  #  Automatic Data Loading


while True:  #  Main Menu

    print("--- Student Record Management ---")
    print("1. Add Student Record.")
    print("2. View All Students Record.")
    print("3. Search for a Student record.")
    print("4. Show Top Student.")
    print("5. Show average grades.")
    print("6. Delete Student's record.")
    print("7. Update Student's record.")
    print("0. Exit System.")

    choice = get_integer("Enter Number(0 - 7): ")

    match choice:
        case 1:
            add_student(students)

        case 2:
            view_students(students)

        case 3:
            search_student(students)

        case 4:
            top_student(students)

        case 5:
            average_grades(students)

        case 6:
            delete_student(students)

        case 7:
            update_student(students)

        case 0:
            save_data(students)
            break  #  Exit ;)
