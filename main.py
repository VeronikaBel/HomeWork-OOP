class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _avg_grade(self):
        if not self.grades:
            return 0
        grades_list = []
        for g in self.grades.values():
            grades_list.extend(g)
        return round(sum(grades_list) / len(grades_list), 2)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self._avg_grade()}\n Курсы в процессе изучения: {self.courses_in_progress}\n Завершенные курсы: {self.finished_courses}'

    def best_student(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
        else:
            return self._avg_grade() < other._avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _avg_grade(self):
        if not self.grades:
            return 0
        grades_list = []
        for g in self.grades.values():
            grades_list.extend(g)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_grade()}'

    def best_lecturer(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self._avg_grade() < other._avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Ruoy', 'Eman', 'male')
student_2 = Student('Kate', 'Ryan', 'female')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Как найти время для обучения']
student_2.courses_in_progress += ['Java']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Вводный модуль']

lecturer_1 = Lecturer('Maria', 'Gomez')
lecturer_2 = Lecturer('Stefan', 'Kirby')

lecturer_1.courses_attached += ['Java']
lecturer_2.courses_attached += ['C++']

reviewer_1 = Reviewer('Sara', 'Parker')
reviewer_2 = Reviewer('Peter', 'Parker')

reviewer_1.courses_attached += ['Java']
reviewer_2.courses_attached += ['Python']

student_1._avg_grade()
student_2._avg_grade()
student_1.rate_lecturer(lecturer_1, 'Java', 9)
student_2.rate_lecturer(lecturer_2, 'C++', 10)
student_1.best_student(student_2)

lecturer_1._avg_grade()
lecturer_2._avg_grade()
lecturer_1.best_lecturer(lecturer_2)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Java', 8)



