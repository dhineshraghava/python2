from student3 import StudentProfile
class StudnentProfile():
    def __init__(self,student_id,name,course,score):
        self.student_id = student_id
        self.name = name
        self.course = course
        self._score = score
    def get_score(self):
        return self._score
    def updated_score(self,new_score):
        if new_score > 0  and new_score < 100:
            self._score = new_score
        else:
            return "Needs pratice"
    def __str__(self):
        return f"{self.student_id}: {self.name} {self.course} {self._score}"
str1 = StudentProfile("dhinesh",101,"python",98)
print(str1._get_score)
print(str1.__str__())