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

