# File Handling *******************************************************************************

Data_File = "record.txt"


def save_data(students):

    with open(Data_File, "w") as file:

        for student in students:
            file.write(
                f"{student['id']},{student['name']},{student['age']},{student['grades']}\n"
            )


def load_data(students):
    try:
        with open(Data_File, "r") as file:

            for line in file:
                line = line.strip()
                parts = line.split(",")
                student = {
                    "id": int(parts[0]),
                    "name": parts[1],
                    "age": int(parts[2]),
                    "grades": float(parts[3]),
                }
                students.append(student)
            print("File loaded successfully :)")

    except FileNotFoundError:
        print("No saved records found. Starting with an empty database.")
