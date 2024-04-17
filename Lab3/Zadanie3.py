import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

print("Studenci: ")
cursor.execute("select * from student")
students = cursor.fetchall()
for student in students:
    print(student)

print("\n Studenci z grupy 1:")
cursor.execute("Select * from student where group_id = 1")
group1Students = cursor.fetchall()
for student in group1Students:
    print(student)

print("\n Studenci z oceną >= 4 z matmy:")
cursor.execute("""
select student.* 
from student
join grade on student.student_id = grade.student_id
where grade.grade >= 4 
""")
studentsGrade4 = cursor.fetchall()
for student in studentsGrade4:
    print(student)

print("\n Wykladowcy: ")
cursor.execute("SELECT name, surname, lecture_id from lecturer ")
lecturers = cursor.fetchall()
for lecturer in lecturers:
    print(lecturer)

print("\n wydzial")
cursor.execute("SELECT faculty.name, student_group.name FROM faculty JOIN student_group ON faculty.faculty_id = student_group.faculty_id")
dane = cursor.fetchall()
for wydzial in dane:
    print(wydzial)

print("\nStudenci z srednia ocen")

cursor.execute(" SELECT Student.student_id, Student.name, Student.surname, AVG(grade.grade) AS avarege FROM Student JOIN grade ON Student.student_id = grade.student_id GROUP BY Student.student_id")
dane = cursor.fetchall()
for student in dane:
    print(student)
