from helpers import get_integer, get_float, get_grades, get_nxt_ID


def add_student(students):
    num = get_integer("(How many students record would you like to add?): ")
    for i in range(num):
        name = input("Enter Name: ")
        age = get_integer("Enter age: ")
        grades = get_grades("Enter Grades: ")

        student = {
            "id": get_nxt_ID(students),
            "name": name,
            "age": age,
            "grades": grades,
        }

        students.append(student)

        print("Student record added successfully!")


def view_students(students):
    if not students:
        print("Student Record is Empty.")
        return

    print(" ID | Name    | Age | Grades ")
    for student in students:
        print(
            f"{student['id']} - {student['name']} - {student['age']} - {student['grades']}"
        )


def search_student(students):
    if not students:
        print("Student Record is Empty.")
        return
    s_id = get_integer("Enter Student ID: ")
    found = False
    for student in students:
        if student["id"] == s_id:
            print("Student Record:")
            print(
                f"{student['id']} - {student['name']} - {student['age']} - {student['grades']}"
            )
            found = True
            break
    # for s in students:             //Later will Improve this feature by adding option for searching by name and ID
    #     if s["name"].lower() == s_name.lower():
    #         print("STUDENT RECORD:")
    #         print(f" {s['name']} - {s['age']} - {s['grades']}")
    #         found = True
    #         break

    if not found:
        print("Student Record Not Found.")


def delete_student(students):
    if not students:
        print("Student Record is Empty.")
        return

    s_id = get_integer("Enter Student ID: ")

    for student in students:
        if student["id"] == s_id:
            students.remove(student)
            print("Student's Record Deleted Successfully..")
            break
    else:
        print("Student's record not found.")


def update_student(students):
    if not students:
        print("Student Record is Empty.")
        return

    s_id = get_integer("Enter Student ID: ")

    for student in students:
        if student["id"] == s_id:
            print("Current Record:")
            print(
                f"{student['id']} - {student['name']} - {student['age']} - {student['grades']}"
            )
            print("\nNow Update the Record: ")

            new_name = input("Enter new name: ")
            new_age = get_integer("Enter new age: ")
            new_grades = get_float("Enter new grades: ")

            student.update({"name": new_name, "age": new_age, "grades": new_grades})

            print("Student's Record Updated Successfully..")
            break
    else:
        print("Student's record not found.")


def top_student(students):
    if not students:
        print("Student Record is Empty.")
        return

    top = students[0]
    for student in students:
        if student["grades"] > top["grades"]:

            top = student

    print(f"{top['id']} - {top['name']} - {top['age']} - {top['grades']}")


def average_grades(students):
    if not students:
        print("Student Record is Empty.")
        return

    grades_sum = 0
    count = 0
    for student in students:
        if student["grades"] >= 0:
            grades_sum += student["grades"]
            count += 1

    avg_grades = grades_sum / count
    print(f"Average grades: {avg_grades:.2f}")
