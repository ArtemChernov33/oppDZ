class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
class Lector:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
 
best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.grades['Git'] = [10, 10, 10, 10, 10]
best_student1.grades['Python'] = [10, 5]
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.grades['Git'] = [10, 10, 5, 10, 10]
best_student.grades['Python'] = [10, 10]
 
print(best_student1.grades)
print(best_student.grades)

lector = Lector('Some', 'Buddy')
lector.grades['Python'] = [3, 10]
print(lector.grades)

lector1 = Lector('Some', 'Buddy')
lector1.grades['Python'] = [8, 10]
print(lector1.grades)

st_list = ['best_student1', 'best_student']
l_list = ['lector', 'lector1']
course_list = best_student.grades
def sos(st_list, course_list):
    sum_grades = 0
    len_grades = 0
    for st in st_list:
        for k, v in course_list.items():
            if k == 'Python':
                sum_grades = sum(v)
                len_grades = len(v)
                sroc = sum_grades / len_grades
                print(f'Средняя оценка студента: {sroc}')               
        break
sos(st_list, course_list)

course_list1 = best_student1.grades
def sos1(st_list, course_list1):
    sum_grades = 0
    len_grades = 0
    for st in st_list:
        for k, v in course_list1.items():
            if k == 'Python':
                sum_grades = sum(v)
                len_grades = len(v)
                sroc = sum_grades / len_grades
                print(f'Средняя оценка студента1: {sroc}')
        break
sos1(st_list, course_list1)

course_list = lector.grades
def sol(st_list, course_list):
    sum_grades = 0
    len_grades = 0
    for st in st_list:
        for k, v in course_list.items():
            if k == 'Python':
                sum_grades = sum(v)
                len_grades = len(v)
                sroc = sum_grades / len_grades
                print(f'Средняя оценка лектора: {sroc}')               
        break
sol(st_list, course_list)

course_list = lector1.grades
def sol1(st_list, course_list):
    sum_grades = 0
    len_grades = 0
    for st in st_list:
        for k, v in course_list.items():
            if k == 'Python':
                sum_grades = sum(v)
                len_grades = len(v)
                sroc = sum_grades / len_grades
                print(f'Средняя оценка лектора1: {sroc}')               
        break
sol1(st_list, course_list)