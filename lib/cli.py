
from helpers import (

    exit_program,
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,
    delete_department,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_department_employees
)


def main():
    while True:
        menu()
        choice = input("> ").strip()
        print()  # Add spacing for better UX

        if choice == "0":
            exit_program()
        elif choice == "1":
            list_departments()
        elif choice == "2":
            find_department_by_name()
        elif choice == "3":
            find_department_by_id()
        elif choice == "4":
            create_department()
        elif choice == "5":
            update_department()
        elif choice == "6":
            delete_department()
        elif choice == "7":
            list_employees()
        elif choice == "8":
            find_employee_by_name()
        elif choice == "9":
            find_employee_by_id()
        elif choice == "10":
            create_employee()
        elif choice == "11":
            update_employee()
        elif choice == "12":
            delete_employee()
        elif choice == "13":
            list_department_employees()
        else:
            print("Invalid choice. Please try again.\n")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all departments")
    print("2. Find department by name")
    print("3. Find department by ID")
    print("4. Create a department")
    print("5. Update a department")
    print("6. Delete a department")
    print("7. List all employees")
    print("8. Find employee by name")
    print("9. Find employee by ID")
    print("10. Create an employee")
    print("11. Update an employee")
    print("12. Delete an employee")
    print("13. List all employees in a department")
    print()


if __name__ == "__main__":
    main()
