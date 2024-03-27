import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''create table university (
university_id integer primary key, 
name text not null
)''')

cursor.execute('''create table faculty (
faculty_id integer primary key,
name text not null,
university_id integer not null,
foreign key (university_id) references university(university_id)
)''')


cursor.execute('''create table student_group (
group_id integer primary key, 
name text not null,
faculty_id integer not null, 
foreign key (faculty_id) references faculty(faculty_id)
)''')

cursor.execute('''create table lecture (
lecture_id integer primary key,
name text not null
)''')


cursor.execute('''create table lecturer (
lecturer_id integer primary key,
name text not null,
surname text not null, 
lecture_id integer not null,
foreign key (lecture_id) references lecture(lecture_id)
)''')

cursor.execute('''create table student (
student_id integer primary key, 
name text not null,
surname text not null, 
group_id integer not null,
foreign key (group_id) references student_group(group_id)
)''')

cursor.execute('''create table grade (
grade_id integer primary key, 
student_id integer not null,
lecture_id integer not null,
grade integer not null, 
foreign key (student_id) references student(student_id),
foreign key (lecture_id) references lecture(lecture_id)
)''')

conn.commit()
conn.close()
