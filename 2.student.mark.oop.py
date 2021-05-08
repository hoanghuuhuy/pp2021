#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Student:
    def __init__(self, id, name, dob):
        self.s_id = id
        self.s_name = name
        self.DoB = dob
        self.marks = {}

    def get_id(self):
        return self.s_id

    def get_name(self):
        return self.s_name

    def get_DoB(self):
        return self.Dob

    def get_mark(self):
        return self.marks

    def set_mark(self, course, mark):
        self.marks.update({course: mark})
    
    def Student_list(self):
        print("Student's ID: " + self.s_id)
        print("Student's name: " + self.s_name)
        print("Student's Date of Birth: " + self.DoB)

    def Mark_list(self, course):
        print(self.s_name + "'s mark: " + str(self.marks.get(course)))


class Course:
    def __init__(self, id, name):
        self.c_id = id
        self.c_name = name

    def get_id(self):
        return self.c_id

    def get_name(self):
        return self.c_name

    def Course_list(self):
        print("Course's ID: " + self.c_id)
        print("Course's name: " + self.c_name)

        
def CountStudent():
    count = int(input("How many students are there: "))
    return count


def student_detail():
    s_id = input("ID: ")
    s_name = input("Name: ")
    DoB = input("Date of birth: ")
    return s_id, s_name, DoB


def CountCourse():
    count = int(input("How many courses are there: "))
    return count


def course_detail():
    c_id = input("ID: ")
    c_name = input("Name: ")
    return c_id, c_name


def Add_mark(courses, c_id):
    for course in courses:
        course.get_id() == c_id
        return course.get_name()


if __name__ == "__main__":
    students = []
    courses = []

    s_number = CountStudent()
    print(s_number)
    for i in range(0, s_number):
        s_id, s_name, DoB = student_detail()
        students.append(Student(s_id, s_name, DoB))

    c_number = CountCourse()
    for i in range(0, c_number):
        c_id, c_name = course_detail()
        courses.append(Course(c_id, c_name))

    x = '1'
    while x == '1':
        choose_course_id = input("Select a course ID: ")
        choose_course = Add_mark(courses, choose_course_id)
        print("Course name: " + choose_course + "\n")
        for student in students:
            mark = input("Enter " + student.s_name + "'s mark: ")
            student.set_mark(choose_course, mark)
        x = input("Do you want to add mark in another course? (1:yes/0:no): ")

    print("All Students: ")
    for student in students:
        student.Student_list()

    print("All Courses: ")
    for course in courses:
        course.Course_list()
        
    choose_course_id = input("Select a course id: ")
    choose_course = Add_mark(courses, choose_course_id)
    print("All marks of the course: ")
    for student in students:
        student.Mark_list(choose_course)


# In[ ]:




