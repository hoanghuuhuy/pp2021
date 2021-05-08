#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import domains
from domains import *
import input
from input import * 
    
def main():
        
if __name__ == "__main__":
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

