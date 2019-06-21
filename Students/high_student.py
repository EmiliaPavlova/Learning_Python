# inheritance
from student import Student


class HighSchoolStudent(Student):
    school_name = 'High School of Free-Spirit students'

    def get_school_name(self):
        return 'This is a High School student'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + ' - HS'
