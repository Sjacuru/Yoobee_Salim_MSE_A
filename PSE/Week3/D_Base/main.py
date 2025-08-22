"""
Week 3 - Activity 5: update the sample code "Sample_code_SQLite3"
Please add a new table named "Students" with three columns: Stu_ID, Stu_name, and Stu_address. 
Insert two sample records into Students, then display all rows from both the Users and Students
tables.
"""

from database import create_table
from database_stu import student_table
from user_manager import add_user, view_users, search_user, delete_user
from student_manager import add_student, view_students, search_student, delete_student

def menu():
    print("\n==== User Manager ====")
    print("1.  Add User")
    print("2.  View All Users")
    print("3.  Search User by Name")
    print("4.  Delete User by ID")
    print("5.  Add Student")
    print("6.  View All Students")
    print("7.  Search student by Name")
    print("8.  Delete Student by ID")
    print("8.  View All Users and Students")
    print("10. Exit")

def main():
    create_table()
    student_table()
    while True:
        menu()
        choice = input("Select an option (1-10): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            student_name = input("Enter name: ")
            student_mail = input("Enter email: ")
            stu_Address = input("Enter address: ")
            add_student(student_name, student_mail, stu_Address)
        elif choice == '6':
            students = view_students()
            for student in students:
                print(student)
        elif choice == '7':
            student_name = input("Enter name to search: ")
            students = search_student(student_name)
            for student in students:
                print(student_name)
        elif choice == '8':
            student_id = int(input("Enter user ID to delete: "))
            delete_student(student_id)
        elif choice == '9':
            print("Active users list")
            users = view_users()
            for user in users:
                print(user)           
            print("Active students list") 
            students = view_students()
            for student in students:
                print(student)
        elif choice == '10':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

            student_id = 0,
            student_name = str(), 
            stu_Address = str() 

if __name__ == "__main__":
    main()
