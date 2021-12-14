class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_Grades = {}
    def add_courses(self, course_name):
        self.finished_course.append(course_name)
        
    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
     sum_grades = 0
     len_grades = 0
     for grades in self.grades.values():
        sum_grades = sum(grades)
        len_grades = len(grades)
        self.average_Grades = sum_grades / len_grades

    def list_course(self):
        self.courses_in_progress = ','.join(self.courses_in_progress)

    def finish_list_course(self):
        self.finished_courses = ','.join(self.finished_courses)

    def __str__(self):
      Name = f'Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценказа домашнее задание: {self.average_Grades} \n' \
              f'Курсы в процессе обучения: {best_student.courses_in_progress} \nЗавершеные курсы: {best_student.finished_courses}'
      return Name

    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
          
class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.courses_in_progress = []
        self.average_Grades = {}

    def average_grades(self):
     sum_grades = 0
     len_grades = 0
     for grades in self.grades.values():
        sum_grades = sum(grades)
        len_grades = len(grades)
        self.average_Grades = sum_grades / len_grades
       
    def __lt__(self, Student):
        return self.grades < Student.grades

    def __str__(self):
      Name = f'Имя:{self.name} \nФамилия:{self.surname} \nСредняя оценка за лекцию:{self.average_Grades}'
      return Name
         
class Reviewer(Mentor):
    def  __init__(self, name, surname):
        Mentor. __init__(self, name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
      Name = f'Имя:{self.name} \nФамилия:{self.surname}'
      return Name

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_in_progress += ['Python']
cool_lecturer.courses_in_progress += ['GIT']
 
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lw(cool_lecturer, 'Python', 9)
best_student.rate_lw(cool_lecturer, 'Python', 9)
best_student.rate_lw(cool_lecturer, 'Python', 10)
best_student.average_grades()
cool_lecturer.average_grades()
best_student.list_course()
best_student.finish_list_course()

print(best_student) 

print()
print(cool_lecturer)
print() 
print(cool_reviewer)
print()

print(cool_lecturer.average_Grades < best_student.average_Grades)