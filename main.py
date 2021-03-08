from shlex import join


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg = 0

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg} ' \
               f'\nКурсы в процессе изучения: {join(self.courses_in_progress)}' \
               f'\nЗавершенные курсы:{join(self.finished_courses)}'

    def add_grade_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            lecturer.avg = averagegrade(lecturer.grades)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            student.avg = averagegrade(student.grades)
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.avg = 0

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avg}'


def averagegrade(grades):
    totalCountGrades = 0
    totalSumGrades = 0
    for subjects in grades.values():
        for grade in subjects:
            totalSumGrades += grade
        totalCountGrades += len(subjects)
    avg = totalSumGrades / totalCountGrades
    return round(avg, 2)


def avg_grade_subj(mans, subject):
    countGrade = 0
    totalGrades = 0
    for element in mans:
        if isinstance(element, Lecturer) or isinstance(element, Student):
            try:
                countGrade += len(element.grades[subject])
                for grades in element.grades[subject]:
                    totalGrades += grades
            except KeyError:
                return 'Такого предмета не существует'
        else:
            return 'Ошибка'
    return totalGrades / countGrade


best_student = Student('Roy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['PHP']
second_student = Student('Bob', 'Smith', 'male')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['PHP']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['PHP']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'PHP', 3)
cool_mentor.rate_hw(best_student, 'PHP', 2)

cool_mentor.rate_hw(second_student, 'Python', 8)
cool_mentor.rate_hw(second_student, 'Python', 7)
cool_mentor.rate_hw(second_student, 'PHP', 10)

bad_lecturer = Lecturer('Ivan', 'Ivanov')
bad_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['PHP']

sad_lecturer = Lecturer('Ivan', 'Popov')
sad_lecturer.courses_attached += ['Python']
sad_lecturer.courses_attached += ['PHP']
best_student.add_grade_lecturer(bad_lecturer, 'Python', 7)
best_student.add_grade_lecturer(bad_lecturer, 'Python', 8)
best_student.add_grade_lecturer(bad_lecturer, 'PHP', 2)

second_student.add_grade_lecturer(sad_lecturer, 'Python', 6)
second_student.add_grade_lecturer(sad_lecturer, 'Python', 3)
second_student.add_grade_lecturer(sad_lecturer, 'PHP', 10)

students = [best_student, second_student]
lecturers = [bad_lecturer, sad_lecturer]
print(second_student)
print(bad_lecturer)
print(avg_grade_subj(students, 'PHP'))
print(avg_grade_subj(lecturers, 'Python'))
