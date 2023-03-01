#!/usr/bin/env python
# coding: utf-8



students_list = []
courses_list = []
class_num = 0
course_num = 0




def add_students():
    n_students= int(input("input the number of students you want to add"))
    for i in range(n_students):
        name = input("name: ")
        student_id = input("id: ")
        DoB = input("DOB(seperated with an /: )")
        student = {"name": name, "id": student_id, "DoB" : DoB}
        students_list.append(student)

def add_courses():
    n_courses= int(input("input the number of courses you want to add"))
    for i in range(n_courses):
        name = input("name: ")
        course_id = input("course id: ")
        course = {"name": name, "id": course_id}
        courses_list.append(course)

def add_students_to_specific_course(id_, course_):
    for i in range(len(id_)):
        if "student" in course_:
            for j in range(len(course_["student"])):
                if id_[i] == course_["student"][j]:
                    print("student " + str(id_[i]) + " already in the course")
                    i = i + 1
                else:
                    course_["student"].append(id_[i])
        else:
            course_["student"] = []
            course_["student"].append(id_[i])
    return course_

def add_students_to_course(course_num):
    course_id = input("input the id of course you want to add students in: ")
    course_students =(input("input the id of the sudents you want to add in(seperated with space): "))
    course_students = course_students.split()
    for i in range(course_num - 1):
        if course_id == courses_list[i]["id"]:
            courses_list[i] = add_students_to_specific_course(course_students, courses_list[i])
def add_scores(course_num):
    course_id = input("input the id of course you want to add scores: ")
    for i in range(course_num - 1):
        if course_id == courses_list[i]["id"]:
            courses_list[i]["score"] = []
            for j in range(len(courses_list[i]["student"])):
                score = int(input(("input score for student ")+ str(courses_list[i]["student"][j])))
                courses_list[i]["score"].append(score)
                
def display_class(class_num):
    print("there are " + str(class_num) + "students in the class: ")
    print(students_list)
def display_course(course_num):
    print("there are " + str(course_num) + "course: ")
    print(courses_list)
def display_specific_course(course_num):
    course_id = input("input the id of the course you want to display: ")
    for i in range(course_num - 1):
        if course_id == courses_list[i]["id"]:
            print(courses_list[i])

def display_a_student(course_num, class_num):
    student_id = input("input the id of the student you want to display: ")
    for i in range(class_num - 1):
        if student_id == students_list[i]["id"]:
            print(students_list[i])
    for i in range(course_num -1):
        for j in range(len(courses_list[i]["student"])):
            if courses_list[i]["student"][j] == student_id :
                print(courses_list[i]["name"],courses_list[i]["id"])
            
    




while True: 
    print("what do you wanna do \n?" 
          "1. add students to class \n"
          "2. add courses \n"
          "3. add students to course \n"
          "4. add scores \n"
          "5. display class \n"
          "6. display course list \n"
          "7. display a course \n"
          "8. display a student \n"
          "9. break")
    choice = int(input("choice : "))
    if(choice == 1):
        add_students()
        class_num = len(students_list)
    elif(choice == 2):
        add_courses()
        course_num = len(courses_list)
    elif(choice == 3):
        add_students_to_course(course_num)
    elif(choice == 4):
        add_scores(course_num)
    elif(choice == 5):
        display_class(class_num)
    elif(choice == 6):
        display_course(course_num)
    elif(choice == 7):
        display_specific_course(course_num)
    elif(choice == 8):
        display_a_student(course_num,class_num)
    elif(choice == 9):
        break
    else:
        choice = int(input("please enter num from 1 to 9"))
    



