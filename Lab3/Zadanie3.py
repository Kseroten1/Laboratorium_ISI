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