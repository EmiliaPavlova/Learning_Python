students = []


class Student:
    school_name = 'First School of Free-Spirit students'

    def __init__(self, name, student_id=0000):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return f'Student {self.name.title()}, id: {self.student_id}'

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
