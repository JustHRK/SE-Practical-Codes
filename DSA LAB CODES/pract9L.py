# Constants for the file path and record size
# Department maintains a student information. The file contains roll number, name, division and address. Allow user to add, delete information of student. Display information of particular employee. If record of student does not exist an appropriate message is displayed. If it is, then the system displays the student details. Use sequential
# file to main the data.


FILE_PATH = "student_info.txt"
RECORD_SIZE = 100

def add_student_info():
    roll_number = input("Enter the roll number: ")
    name = input("Enter the name: ")
    division = input("Enter the division: ")
    address = input("Enter the address: ")

    # Create the formatted record string
    record = f"{roll_number},{name},{division},{address}\n"

    # Append the record to the file
    with open(FILE_PATH, "a") as file:
        file.write(record)

    print("Student information added successfully.")

def delete_student_info():
    roll_number = input("Enter the roll number to delete: ")

    # Read all records from the file
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()

    # Find and remove the record with the specified roll number
    updated_lines = []
    deleted = False

    for line in lines:
        if line.startswith(roll_number + ","):
            deleted = True
        else:
            updated_lines.append(line)

    # Write the updated records back to the file
    with open(FILE_PATH, "w") as file:
        file.writelines(updated_lines)

    if deleted:
        print("Student information deleted successfully.")
    else:
        print("Student information not found.")

def display_student_info():
    roll_number = input("Enter the roll number to display: ")

    # Read the records from the file
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()

    # Find and display the record with the specified roll number
    found = False

    for line in lines:
        if line.startswith(roll_number + ","):
            found = True
            record = line.strip().split(",")
            print("Roll Number:", record[0])
            print("Name:", record[1])
            print("Division:", record[2])
            print("Address:", record[3])
            break

    if not found:
        print("Student information not found.")


# Main menu loop
while True:
    print("\n***** Student Information System *****")
    print("1. Add Student Information")
    print("2. Delete Student Information")
    print("3. Display Student Information")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student_info()
    elif choice == "2":
        delete_student_info()
    elif choice == "3":
        display_student_info()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Student Information System.")
