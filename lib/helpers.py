from models.department import Department
from models.employee import Employee
from config import session  # Make sure your DB session is accessible here

def exit_program():
    print("Goodbye!")
    exit()

# ===== Department Functions =====

def list_departments():
    departments = session.query(Department).all()
    for dept in departments:
        print(f"[{dept.id}] {dept.name} - {dept.location}")

def find_department_by_name():
    name = input("Enter department name: ")
    dept = session.query(Department).filter_by(name=name).first()
    if dept:
        print(f"[{dept.id}] {dept.name} - {dept.location}")
    else:
        print("Department not found.")

def find_department_by_id():
    try:
        id = int(input("Enter department ID: "))
        dept = session.query(Department).get(id)
        if dept:
            print(f"[{dept.id}] {dept.name} - {dept.location}")
        else:
            print("Department not found.")
    except ValueError:
        print("Invalid input.")

def create_department():
    name = input("Enter department name: ")
    location = input("Enter department location: ")
    dept = Department(name=name, location=location)
    session.add(dept)
    session.commit()
    print(f"Department '{name}' created successfully.")

def update_department():
    try:
        id = int(input("Enter department ID to update: "))
        dept = session.query(Department).get(id)
        if dept:
            dept.name = input(f"New name (current: {dept.name}): ") or dept.name
            dept.location = input(f"New location (current: {dept.location}): ") or dept.location
            session.commit()
            print("Department updated successfully.")
        else:
            print("Department not found.")
    except ValueError:
        print("Invalid input.")

def delete_department():
    try:
        id = int(input("Enter department ID to delete: "))
        dept = session.query(Department).get(id)
        if dept:
            session.delete(dept)
            session.commit()
            print("Department deleted.")
        else:
            print("Department not found.")
    except ValueError:
        print("Invalid input.")

# ===== Employee Functions =====

def list_employees():
    employees = session.query(Employee).all()
    for emp in employees:
        print(f"[{emp.id}] {emp.name}, {emp.job_title}, Dept ID: {emp.department_id}")

def find_employee_by_name():
    name = input("Enter employee name: ")
    emp = session.query(Employee).filter_by(name=name).first()
    if emp:
        print(f"[{emp.id}] {emp.name}, {emp.job_title}, Dept ID: {emp.department_id}")
    else:
        print("Employee not found.")

def find_employee_by_id():
    try:
        id = int(input("Enter employee ID: "))
        emp = session.query(Employee).get(id)
        if emp:
            print(f"[{emp.id}] {emp.name}, {emp.job_title}, Dept ID: {emp.department_id}")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input.")

def create_employee():
    name = input("Enter employee name: ")
    job_title = input("Enter job title: ")
    try:
        department_id = int(input("Enter department ID: "))
        emp = Employee(name=name, job_title=job_title, department_id=department_id)
        session.add(emp)
        session.commit()
        print(f"Employee '{name}' created.")
    except ValueError:
        print("Invalid department ID.")

def update_employee():
    try:
        id = int(input("Enter employee ID to update: "))
        emp = session.query(Employee).get(id)
        if emp:
            emp.name = input(f"New name (current: {emp.name}): ") or emp.name
            emp.job_title = input(f"New job title (current: {emp.job_title}): ") or emp.job_title
            try:
                dept_input = input(f"New department ID (current: {emp.department_id}): ")
                if dept_input:
                    emp.department_id = int(dept_input)
            except ValueError:
                print("Invalid department ID input, keeping previous value.")
            session.commit()
            print("Employee updated.")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input.")

def delete_employee():
    try:
        id = int(input("Enter employee ID to delete: "))
        emp = session.query(Employee).get(id)
        if emp:
            session.delete(emp)
            session.commit()
            print("Employee deleted.")
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid input.")

def list_department_employees():
    try:
        dept_id = int(input("Enter department ID: "))
        dept = session.query(Department).get(dept_id)
        if dept:
            employees = session.query(Employee).filter_by(department_id=dept_id).all()
            print(f"Employees in {dept.name}:")
            for emp in employees:
                print(f"[{emp.id}] {emp.name}, {emp.job_title}")
        else:
            print("Department not found.")
    except ValueError:
        print("Invalid input.")
