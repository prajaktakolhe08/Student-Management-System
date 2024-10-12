from admin import Admin
from student import Student
from tabulate import tabulate
import emoji

def student_login(a):
    print(emoji.emojize(":student: Student Login"))
    student_id = input("Enter Student ID: ")
    password = input("Enter Password: ")
    student = a.search_student(student_id)
    if student and student_id == password: 
        print(emoji.emojize(":check_mark_button: Login successful!")) 
        return student
    else:
        print(emoji.emojize(":cross_mark: Invalid login credentials."))
        return None

def admin_login(a):
    print(emoji.emojize(":locked_with_key: Admin Login"))
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")
    
    if a.login(username,password):
        print(emoji.emojize(":check_mark_button: Login successful!"))
        return True
    else:
        print(emoji.emojize(":cross_mark: Invalid login credentials."))
        return False
def display_student_details(student):
    headers = ["Student ID","Name","Address","Phone","Course","Grades"]
    data = [[student.student_id, student.name, student.address, student.phone, student.course, student.grades]]
    print(tabulate(data,headers,tablefmt="grid"))
        
def student_menu(a,student):
    
    while True:
        print(emoji.emojize(":memo: Student Menu"))
        print("\t\t1. Update Profile")
        print("\t\t2. View Details")
        print("\t\t3. view Grades")
        print("\t\t4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            student_id = input("Enter Student ID: ")
            student = a.search_student(student_id)
            if student:
                address = input("Enter New Address: ")
                phone = int(input("Enter New Phone: "))
                student.update_profile(address, phone)
                a.update_student_record(student)
                print("Profile updated.")
            else:
                print("Student not found.")
            
        elif choice == 2:
            if student:
                display_student_details(student)
            else:
                print("Student not found.")  
                
        elif choice == 3:
            student_id = input("Enter Student ID: ")
            student = a.search_student(student_id)
            if student:
                print("Grades:", student.view_grades())
            else:
                print("Student not found.")        
                
        elif choice == 4:
            break
        else:
            print(emoji.emojize(":warning: Invalid Choice!!"))

def admin_menu(a):
  
    while True:
        print(emoji.emojize(":hammer_and_wrench: Admin Menu"))
        print("\t\t1. Add Student")    
        print("\t\t2. Edit Student Details") 
        print("\t\t3. Delete Student") 
        print("\t\t4. search Student") 
        print("\t\t5. Display All Students") 
        print("\t\t6. Assign Grades") 
        print("\t\t7. Exit")    
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            address = input("Enter address: ")
            phone = input("Enter phone: ")
            course = input("Enter Course: ")
            student = Student(student_id,name,address,phone,course)               
            a.add_student(student)
            
        elif choice == 2:
            student_id = input("Enter Student ID: ")
            student = a.search_student(student_id)
            if student:
                name = input("Enter New Name: ")
                address = input("Enter New Address: ")
                phone = input("Enter New Phone: ")
                course = input("Enter New Course: ")
                student.name = name
                student.address = address
                student.phone = phone
                student.course = course
                a.update_student_record(student)
                print("Student details updated.")
            else:
                print("Student not found.")
            
        elif choice == 3:
            student_id = input("Enter Student ID: ")
            a.delete_student(student_id)
            
        elif choice == 4:
            student_id = input("Enter Student ID: ")
            student = a.search_student(student_id)
            if student:
                display_student_details(student)
            else:
                print("Student not found.")
            
        elif choice == 5:
            print(emoji.emojize(":books: All Students"))
            a.show_all_students()
            
        elif choice == 6:
            student_id = input("Enter Student ID: ")
            subject = input("Enter Subject: ")
            grade = input("Enter Grade: ")
            a.assign_grades(student_id,subject,grade) 
            
        elif choice == 7:
            break
        else:
            print(emoji.emojize(":warning: Invalid Choice!!"))
            
def main():
    a = Admin()
    while True:
        print(emoji.emojize(":school: Student Management System"))
        print("\t\t1. Student Menu")
        print("\t\t2. Admin Menu")
        print("\t\t3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            student = student_login(a)
            if student:
                student_menu(a,student)
            
        elif choice == 2:
            if admin_login(a):
                admin_menu(a) 
            
        elif choice == 3:
            print("👋 Goodbye!")
            break
        else:
            print(emoji.emojize(":warning: Invalid Choice!!"))  
            
if __name__ == "__main__":
    main() 
