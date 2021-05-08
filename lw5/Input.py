#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from domains import *

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

