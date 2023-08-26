# Direct access file (simulated using a dictionary)
# Implementation of a direct access file -Insertion and deletion of a record from a direct access file

direct_access_file = {}

def insert_record():
    roll_number = input("Enter the roll number: ")
    name = input("Enter the name: ")
    division = input("Enter the division: ")
    address = input("Enter the address: ")

    record = {
        "name": name,
        "division": division,
        "address": address
    }

    direct_access_file[roll_number] = record
    print("Record inserted successfully.")

def delete_record():
    roll_number = input("Enter the roll number to delete: ")

    if roll_number in direct_access_file:
        del direct_access_file[roll_number]
        print("Record deleted successfully.")
    else:
        print("Record not found.")

def display_record():
    roll_number = input("Enter the roll number to display: ")

    if roll_number in direct_access_file:
        record = direct_access_file[roll_number]
        print("Roll Number:", roll_number)
        print("Name:", record["name"])
        print("Division:", record["division"])
        print("Address:", record["address"])
    else:
        print("Record not found.")


# Main menu loop
while True:
    print("\n***** Direct Access File *****")
    print("1. Insert Record")
    print("2. Delete Record")
    print("3. Display Record")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        insert_record()
    elif choice == "2":
        delete_record()
    elif choice == "3":
        display_record()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Direct Access File.")
