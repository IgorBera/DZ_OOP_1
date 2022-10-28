class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def lecturer_ratings(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_grade(self):
        total_len = 0
        total_grade = 0
        for key, value in self.grades.items():
            total_len += len(value)
            total_grade += sum(value)
        return f'{total_grade / total_len :.2}'

    def __str__(self):
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}"
                f"\nСредняя оценка за домашние задания: {self.__average_grade()}"
                f"\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}"
                f"\nЗавершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__average_grade() < other.__average_grade()
        return print("This is not student!!!")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_grade(self):
        total_len = 0
        total_grade = 0
        for key, value in self.grades.items():
            total_len += len(value)
            total_grade += sum(value)
        return f'{total_grade / total_len :.2}'

    def __str__(self):
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}"
                f"\nСредняя оценка за лекции: {self.__average_grade()}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise NameError("This is not lecturer!!!")
        return self.__average_grade() < other.__average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
                course in self.courses_attached and\
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}"
                f"\nФамилия: {self.surname}")


def student_comparison(list_st, major):
    total_len = 0
    total_grade = 0
    for student in list_st:
        if major in student.grades:
            total_len += len(student.grades[major])
            total_grade += sum(student.grades[major])
    return print(f'Средний балл студентов по {major}: {total_grade / total_len :.2}')


def lecturer_comparison(list_lec, major):
    total_len = 0
    total_grade = 0
    for lecturer in list_lec:
        if major in lecturer.grades:
            total_len += len(lecturer.grades[major])
            total_grade += sum(lecturer.grades[major])
    return print(f'Средний балл лекторов по {major}: {total_grade / total_len :.2}')


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в програмирование']
student2 = Student('Sofia', 'Stoch', 'your_gender')
student2.courses_in_progress += ['Go']
student3 = Student('Bags', 'Bunny', 'your_gender')
student3.courses_in_progress += ['Git']
student3.courses_in_progress += ['Python']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer2 = Reviewer('Vasiliy', 'Petrow')
reviewer2.courses_attached += ['Git']
reviewer2.courses_attached += ['Go']

lecturer1 = Lecturer('Bob', 'Lucky')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Git']
lecturer2 = Lecturer('Ben', 'Geiz')
lecturer2.courses_attached += ['Go']
lecturer2.courses_attached += ['Python']

student1.lecturer_ratings(lecturer1, 'Python', 9)
student1.lecturer_ratings(lecturer1, 'Python', 9)
student1.lecturer_ratings(lecturer1, 'Git', 8)
student1.lecturer_ratings(lecturer1, 'Git', 8)
student2.lecturer_ratings(lecturer2, 'Go', 5)
student2.lecturer_ratings(lecturer2, 'Go', 7)
student1.lecturer_ratings(lecturer2, 'Python', 1)
student1.lecturer_ratings(lecturer2, 'Python', 1)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student1, 'Git', 7)
reviewer2.rate_hw(student2, 'Go', 10)
reviewer2.rate_hw(student2, 'Go', 5)
reviewer2.rate_hw(student3, 'Git', 3)
reviewer2.rate_hw(student3, 'Git', 3)
reviewer1.rate_hw(student3, 'Python', 1)
reviewer1.rate_hw(student3, 'Python', 9)
reviewer1.rate_hw(student3, 'Python', 1)

print(f'student1: {student1.grades}')
print(f'student2: {student2.grades}')
print(f'student3: {student3.grades}')
print(f'lecturer1: {lecturer1.grades}')
print(f'lecturer2: {lecturer2.grades}')
# print(reviewer1)
# print(student1)
# print(lecturer2)
# print(lecturer2 < lecturer1)
# print(student1 < student2)
students = [student1, student2, student3]
lecturers = [lecturer1, lecturer2]
student_comparison(students, 'Git')
lecturer_comparison(lecturers, 'Python')