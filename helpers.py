# Helper Functions ****************************************************************************


def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid Input :( -> Please enter a number.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid Input :( -> Please enter a number.")


def get_grades(prompt):
    while True:
        value = get_float(prompt)
        if value >= 0 and value <= 100:
            return value
        print("Grades must be between 0 and 100.")


def get_nxt_ID(students):

    max_id = 0
    for student in students:
        if student["id"] > max_id:
            max_id = student["id"]

    return max_id + 1
