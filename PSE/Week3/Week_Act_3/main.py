
from database_subj import create_subj_tb
from database_lect import create_lect_tb
from database_stud import create_stud_tb
from database_clas import create_clas_tb
from subj_manager import add_subject, view_subjects
from lect_manager import add_lecturer, view_lecturers
from stud_manager import add_student, view_students
from clas_manager import add_class, view_classes

def menu():
    print("\n==== College Manager ====")
    print("1.  Add Subjects")
    print("2.  View All Subjects")
    print("3.  Add Lecturer")
    print("4.  View All Lecturers")
    print("5.  Add Student")
    print("6.  View All Students")
    print("7.  Add Class")
    print("8.  View All Classes")
    print("9.  View All Tables")
    print("10. Exit")

def main():
    create_subj_tb()
    create_lect_tb()
    create_stud_tb()
    create_clas_tb()
    while True:
        menu()
        choice = input("Select an option (1-10): ")
        if choice == '1':
            subject_name = input("Enter subject name: ")
            subject_desc = input("Enter subject description: ")
            add_subject(subject_name, subject_desc)
        elif choice == '2':
            subjects = view_subjects()
            for subject in subjects:
                print(subject)
        elif choice == '3':
            lecturer_name = input("Enter lecturer name: ")
            lecturer_email = input("Enter lecturer e-mail: ")
            add_lecturer(lecturer_name, lecturer_email)
        elif choice == '4':
            lecturers = view_lecturers()
            for lecturer in lecturers:
                print(lecturer)
        elif choice == '5':
            student_name = input("Enter name: ")
            student_mail = input("Enter email: ")
            add_student(student_name, student_mail)
        elif choice == '6':
            students = view_students()
            for student in students:
                print(student)
        elif choice == '7':
            class_name = input("Enter tha Class name: ")
            add_class(class_name)
        elif choice == '8':
            classes = view_classes()
            for class_ in classes:
                print(class_)
        elif choice == '9':
            print("Subjects list")
            subjects = view_subjects()
            for subject in subjects:
                print(subject)
            print("Lecturers list")
            lecturers = view_lecturers()
            for lecturer in lecturers:
                print(lecturer)
            print("Students list") 
            students = view_students()
            for student in students:
                print(student)
            print("Classes list") 
            classes = view_classes()
            for class_ in classes:
                print(class_)
        elif choice == '10':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


            subject_name = str(),
            student_name = str(), 
            student_mail = str(),
            class_name = str(),
            lecturer_name = str() 

if __name__ == "__main__":
    main()
