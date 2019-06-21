from student import Student
from high_student import HighSchoolStudent

mark = Student('mark')
print(mark)

print(Student.school_name)

james = HighSchoolStudent('james')
print(james.get_name_capitalize())
print(james.get_school_name())
print(HighSchoolStudent.school_name)
