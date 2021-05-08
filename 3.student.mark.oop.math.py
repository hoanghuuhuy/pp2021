#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import numpy as np


class Student:
    def __init__(self, id, name, dob):
        self.s_id = id
        self.s_name = name
        self.DoB = dob
        self.gpa = 0
        self.marks = np.array([[], [], []])

    def get_id(self):
        return self.s_id

    def get_name(self):
        return self.s_name

    def get_DoB(self):
        return self.Dob

    def get_mark(self):
        return self.marks

    def set_mark(self, course, mark, credit):
        self.marks = np.append(self.marks, [[course], [mark], [credit]], axis=1)

    def get_gpa(self):
        sum_credits = 0
        for i in range(len(courses)):
            self.gpa += int(self.marks[1][i]) * int(self.marks[2][i])
            sum_credits += int(self.marks[2][i])

        self.gpa = math.floor((self.gpa/sum_credits) * 10) / 10
        return self.gpa

    def Student_list(self):
        print("Student's ID: " + self.s_id)
        print("Student's name: " + self.s_name)
        print("Student's Date of Birth: " + self.DoB)
        print("Student's GPA: " + str(self.gpa))


class Course:
    def __init__(self, id, name, credit):
        self.c_id = id
        self.c_name = name
        self.credit = credit

    def get_id(self):
        return self.c_id

    def get_name(self):
        return self.c_name

    def get_credit(self):
        return self.credit

    def Course_list(self):
        print("Course's ID: " + self.c_id)
        print("Course's name: " + self.c_name)
        print("Course's credit: " + self.credit)


def CountStudent():
    count = int(input("How many students are there: "))
    return count


def student_detail():
    s_id = input("ID: ")
    s_name = input("Name: ")
    DoB = input("Date of birth: ")
    return s_id, s_name, DoB

def Gpa_sort():
    s_sorted = sorted(students, key=lambda student: student.gpa, reverse=True)
    for student in s_sorted:
        student.Student_list()
        
def CountCourse():
    count = int(input("How many courses are there: "))
    return count


def course_detail():
    c_id = input("ID: ")
    c_name = input("Name: ")
    credit = input("Credit: ")
    return c_id, c_name, credit

def Credit(courses, c_id):
    for course in courses:
        course.get_id() == c_id
        return course.get_credit()

def Add_mark(courses, c_id):
    for course in courses:
        course.get_id() == c_id
        return course.get_name()

if __name__ == "__main__":
    students = []
    courses = []

    s_number = CountStudent()
    for i in range(0, s_number):
        s_id, s_name, DoB = student_detail()
        students.append(Student(s_id, s_name, DoB))

    c_number = CountCourse()
    for i in range(0, c_number):
        c_id, c_name, credit = course_detail()
        courses.append(Course(c_id, c_name, credit))

    x = '1'
    while x == '1':
        choose_course_id = input("Select a course ID: ")
        choose_course = Add_mark(courses, choose_course_id)
        choose_credit = Credit(courses, choose_course_id)
        print("Course name: " + choose_course + "\n")
        for student in students:
            mark = input("Enter " + student.s_name + "'s mark: ")
            student.set_mark(choose_course, mark, choose_credit)
        x = input("Do you want to add mark in another course? (1:yes/0:no): ")
    
    
        
    print("All students: ")
    for student in students:
        student.get_gpa()
    Gpa_sort()
    
    print("All courses: ")
    for course in courses:
        course.Course_list()

