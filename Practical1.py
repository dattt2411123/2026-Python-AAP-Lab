students = []
courses = []
marks = {}
f = open("students.txt", "w")
t = open("courses.txt", "w")
m = open("marks.txt", "w")
def input_in4():
    #get the information of courses and students
    n = int(input("The number of the student in a class: "))
    c = int(input("The number of the courses: "))
    
    for i in range(n):
        id = int(input("student ID: "))
        name = (input("The name: "))
        DoB = (input("dd/mm/yy: " ))
        student = {'id': id,
                   'name': name,
                   'DoB': DoB}
        students.append(student)
    for i in range(c):
        id_c = int(input("ID Course:" ))
        name_c = (input("The course:"))
        course = {'id': id_c,
                  "name": name_c}
        courses.append(course)

def list_students():
    #list the students to the screen
    for student in students:
        f.write(str(students)) #write the list of in4-student into the file student.txt
        print('ID student',student['id'], student['name'], student['DoB'])
def list_courses():
    #list the courses to the screen
    for course in courses:
        t.write(str(courses))
        print('ID Course',course['id'],':', course['name'])
def mark_id():
    #get mark and select mark for the student
    course_id = int(input("Enter the ID Course:"))
    marks[course_id] ={}
    for student in students:
        mark = float(input("Enter mark for ID_Student: " + str(student['id'] + " ")))
        marks[course_id][student['id']] = mark
def show_marks():

    course_id = int(input("Enter ID Course: "))
    if course_id in marks:
        for student in students:
            student_id = student['id']
            if student_id in marks[course_id]:
                m.write(str(marks))
                print('The mark of the student',
                    student['name'],
                    ":",
                    marks[course_id][student_id]
                )
    else:
        print("No marks")



#run modules
input_in4()
list_students()
list_courses()
mark_id()
show_marks()
