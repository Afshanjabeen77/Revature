# main.py

from functions import *
from crud_operations import *

def main():
    conn = connect_to_database()
    role = input("Enter your role (1 for Administrator, 2 for User): ")

    while True:
        print("\nOperations:")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. Display Data")
        print("5. Exit")

        operation = input("Enter the operation number you want to perform: ")

        if operation == '1' and role == '1':  # Insert Data
            perform_insert(conn)

        elif operation == '2' and role == '1':  # Update Data
            perform_update(conn)

        elif operation == '3' and role == '1':  # Delete Data
            perform_delete(conn)

        elif operation == '4':  # Display Data
            perform_display(conn)

        elif operation == '5':  # Exit
            break

        else:
            print("Invalid operation. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
