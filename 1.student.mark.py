#!/usr/bin/env python
# coding: utf-8

# In[2]:


students = []
courses = []
marks = []


#number of students
def CountStudent():
    count = int(input("How many students are there: "))
    return count


#students' infor
def Students_detail():
    print("Enter Student's information:")
    s_id = input("ID: ")
    s_name = input("Name: ")
    DoB = input("Date of birth: ")
    return s_id, s_name, DoB


#display student list
def Students_list():
    for i in range(len(students)):
        print("Student's ID: " + students[i].get("id"))
        print("Student's name: " + students[i].get("name"))
        print("Student's Date of Birth: " + students[i].get("dob"))

        
#number of courses        
def CountCourse():
    count = int(input("How many courses are there: "))
    return count


#course's infor
def Courses_detail():
    print("Enter Course's information: ")
    c_id = input("ID: ")
    c_name = input("Name: ")
    return c_id, c_name


#display couses' list
def Courses_list():
    for i in range(len(courses)):
        print("Course's ID: " + courses[i].get("id"))
        print("Course's name: " + courses[i].get("name"))


#enter marks
def Mark(students, course):
    for i in range(len(students)):
        marks.append({course: {}})
        mark = float(input("Enter " + students[i].get("name") + "'s mark:\n"))
        marks[i].update({course: mark})


#display marks' list
def Marks_list():
    for i in range(len(students)):
        print(students[i].get("name") + "'s mark:")
        print(marks[i].get(choose_course))
        print("\n")

        
if __name__ == "__main__":
    s_number = CountStudent()
    print(s_number)
    for i in range(0, s_number):
        s_id, s_name, DoB = Students_detail()
        students.append({"id": s_id, "name": s_name, "dob": DoB})

    c_number = CountCourse()
    for i in range(0, c_number):
        c_id, c_name = Courses_detail()
        courses.append({"id": c_id, "name": c_name})

    x = '1'
    while x == '1':
        choose_course_id = input("Select a course ID: ")
        for i in range(len(courses)):
            if courses[i].get("id") == choose_course_id:
                print("Course's name: " + courses[i].get("name") + "\n")
                Mark(students, courses[i].get("name"))
        x = input("Do you want to add mark in another course? (1:yes/0:no): ")

        
    print("All Students: ")
    Students_list()
    print("All Courses: ")
    Courses_list()

    
    choose_course = input("Select a course name: ")
    print("All marks of the course: ")
    Marks_list()


# In[ ]:




