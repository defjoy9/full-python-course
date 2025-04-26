# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:
    count = 0
    total_gpa = 0
    
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls): #cls = class
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_avarage_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Avarage gpa: {cls.total_gpa / cls.count:.2f}"


student1 = Student("Spongebob", 3.2)
student1 = Student("Patric", 2.0)
student1 = Student("Sandy", 4.0)
print(Student.get_count())

print(Student.get_avarage_gpa())