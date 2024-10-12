class Student:
    def __init__(self,student_id,name,address,phone,course):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.grades = {}
        
    def __str__(self):
        return f"{self.student_id},{self.name},{self.address},{self.phone},{self.course},{self.grades}"
    
    def update_profile(self,address=None,phone=None):
        if address:
            self.address = address
        if phone:
            self.phone = phone
            
    def view_grades(self):
        return self.grades
    
    def assign_grade(self,subject,grade):
        self.grades[subject] = grade                       