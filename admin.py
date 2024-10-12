from student import Student

class Admin:
    def __init__(self):
        self.admin_credentials = {"admin": "admin@123"}  
        
    def login(self,username,password):
        return self.admin_credentials.get(username) == password
    
    def add_student(self,student):
        with open("studentData.txt","a") as fp:
            fp.write(str(student) + "\n")
            
    def show_all_students(self):
        try:
            with open("studentData.txt","r") as fp:
                data = fp.read()
                print(data)
                
        except FileNotFoundError:
            print("File is not present")
            
    def search_student(self, student_id):
        try:
            with open("studentData.txt", "r") as fp:
                for student in fp:
                    student_data = student.strip().split(",")
                    if student_id == student_data[0]:
                    
                        student_info = student_data[:5]
                        grades_str = ",".join(student_data[5:]).strip()
                        try:
                            grades = eval(grades_str)
                        except SyntaxError:
                            print(f"Error: Invalid grade data for student ID {student_id}.")
                            grades = {}
                        student_obj = Student(*student_info)
                        student_obj.grades = grades
                        return student_obj
        except FileNotFoundError:
            print("File is not present.")
        return None
    
    def update_student_record(self, updated_student):
        try:
            all_students = []
            with open("studentData.txt", "r") as fp:
                for student in fp:
                    student_data = student.strip().split(",")
                    if updated_student.student_id == student_data[0]:
                        all_students.append(str(updated_student))
                    else:
                        all_students.append(student.strip())
            
            with open("studentData.txt", "w") as fp:
                for student in all_students:
                    fp.write(student + "\n")
        except FileNotFoundError:
            print("File is not present.")   
      
    def delete_student(self,student_id):
        try:
            all_students = [] 
            found = False
            with open("studentData.txt","r") as fp:
                for student in fp:
                    student_data = student.strip().split(",")
                    if student_id != student_data[0]:
                        all_students.append(student.strip()) 
                    else:
                        found = True
                        
            if found:
                with open("studentData.txt","w") as fp:
                    for student in all_students:
                        fp.write(student + "\n")
                print("Record deleated") 
            else:
                print("Record not found.")
        except FileNotFoundError:
            print("File is not present.")  
            
    def assign_grades(self, student_id, subject, grade):
        student = self.search_student(student_id)
        if student:
            student.assign_grade(subject, grade)
            self.update_student_record(student)
            print("Grade assigned.")
        else:
            print("Record not found.")                   
                                                                           