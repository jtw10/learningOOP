# Learning Object-Oriented Programming in Python 3
import datetime


class BigBrain:

    # number of objects in this class
    num_bigbrains = 0

    # class viarbale which dictates the iq growth rate
    iq_growth = 1.01

    def __init__(self, first, last, iq):
        self.first = first
        self.last = last
        self.iq = iq

        # every time a new instance of BigBrain is initiated, increment total by 1
        BigBrain.num_bigbrains += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def raise_iq(self):
        self.iq = int(self.iq * self.iq_growth)

    @classmethod
    def set_iq_growth(cls, amount):
        cls.iq_growth = amount

    @classmethod
    def from_string(cls, bb_str):
        first, last, iq = bb_str.split('-')
        return cls(first, last, iq)  # this line creates a new object

    @staticmethod
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False


bb_1 = BigBrain('dhruv', 'ppap', 9001)
bb_2 = BigBrain('jim', 'bob', 9001)

bb_str_1 = 'jimbob1-bob-9001'
bb_str_2 = 'jimbob2-bob-9001'
bb_str_3 = 'jimbob3-bob-9001'

new_bb_1 = BigBrain.from_string(bb_str_1)
print(new_bb_1.first)

"""
The two following lines of code will print the same result.
print(bb_1.fullname())
print(BigBrain.fullname(bb_1))
"""

BigBrain.set_iq_growth(1.05)

print(BigBrain.iq_growth)
print(bb_1.iq_growth)
print(bb_2.iq_growth)

# 2019-08-13 is a tuesday, so the BigBrain.is_weekend() of this date should return false
my_date = datetime.date(2019, 8, 13)
print(BigBrain.is_weekend(my_date))


# student is a subclass of BigBrain, and it inherits from this class
class Student(BigBrain):

    # by changing the growth rate of a subclass, it doesn't change anything in parent class
    iq_growth = 1.05

    # when we want to init subclass with more variables, we must give Students its own init method
    def __init__(self, first, last, iq, gpa):

        # the BigBrains init method will handle the first name, last name, and iq
        super().__init__(first, last, gpa)

        # the Student subclass will handle the gpa only during the init
        self.gpa = gpa

# Instructor is another subclass of BigBrain


class Instructor(BigBrain):

    # pass a list of students as an argument, but mutable variables should not be passed as an arg, so students=None
    def __init__(self, first, last, iq, students=None):
        super().__init__(first, last, iq)

        # if there are no students, set it to an empty list. otherwise students = students
        if students is None:
            self.students = []
        else:
            self.students = students

    # a method to add students
    def add_stud(self, stud):
        if stud not in self.students:
            self.students.append(stud)

    # a method to remove students
    def rem_stud(self, stud):
        if stud in self.students:
            self.students.remove(stud)

    # method to print out all students under this instructor
    def print_student_list(self):
        for stud in self.students:
            print('-->', stud.fullname())


student1 = Student('dhruv', 'ppap', 9001, 4.3)
student2 = Student('jim', 'bobby', 9001, 4.3)

instructor1 = Instructor('little', 'benjamin', 9001, [student1])

print(student1.first)
print(student2.first)
print(instructor1.fullname())

instructor1.add_stud(student2)
instructor1.print_student_list()

# help function shows method resolution order, where python searches for attributes and methos
# print(help(Student))

""" 
isinstance() tells us if object is isntance of a class
for example, the following would return true true false: 
isinstance(instructor1, Instructor)
isinstance(instructor1, BigBrain)
isinstance(instructor1, Student)

instructor1 is an instance of instructor
instructor1 is an instance of bigbrain, since instructor is subclass of bigbrain
instructor1 is not an instance of a student
"""
print(isinstance(instructor1, Instructor))
print(isinstance(instructor1, BigBrain))
print(isinstance(instructor1, Student))

"""
issubclass() tells us if something is an subclass of something else
for example, the following would return true true false:
issubclass(Instructor, BigBrain)
issubclass(Student, BigBrain)
issubclass(BigBrain, Instructor)

Instructor and Student are subclass of BigBrain
BigBrain is not a subclass of Instructor
"""
print(issubclass(Instructor, BigBrain))
print(issubclass(Student, BigBrain))
print(issubclass(BigBrain, Instructor))
