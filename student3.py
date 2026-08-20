class StudentProfile():
    def __init__(self,name,student_id,course,email,skills):
        self.name = name 
        self.student_id = student_id
        self.course = course
        self.email = email
        self.skills = skills
s1 = StudentProfile("raghava",101,"python","dhineshraghav09@gmail.com",["python","java","git"])
print(s1.name)
print(s1.student_id)
print(s1.course)
print(s1.email)
print(s1.skills)