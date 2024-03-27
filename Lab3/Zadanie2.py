import sqlite3

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute("insert into university (name) values ('Akademia Marynarki Wojennej')")

cursor.execute("insert into faculty (name, university_id) values ('Wydział Informatyki', 1)")
cursor.execute("insert into faculty (name, university_id) values ('Wydział Polonistyki', 1)")

lectures = [
    ('Maths',),
    ('Psychics',),
    ('IT',),
    ('Polish',),
    ('Music',),
    ('Phylosophy',)
]

cursor.executemany("insert into lecture (name) values (?)", lectures)

lecturers = [
    ('Michał', 'Kowalski', 1),
    ('Adam', 'Ksartowski', 2),
    ('Piotr', 'Michałkowski', 3),
    ('Marcin', 'Konrad', 4),
    ('Jan', 'Świerczewski', 5)
]
cursor.executemany("insert into lecturer (name, surname, lecture_id) values (?, ?, ?)", lecturers)

cursor.execute("insert into student_group (name, faculty_id) values ('Grupa 1', 1)")
cursor.execute("insert into student_group (name, faculty_id) values ('Grupa 2', 2)")

students = [
    ('Michał', 'Komin', 1),
    ('Adam', 'Krzesło', 1),
    ('Jarosław', 'Kaczka', 1),
    ('Donald', 'Traitor', 2),
    ('Grzegorz', 'Brązowy', 2),
    ('Andrzej', 'Tatowski', 2)
]

cursor.executemany("insert into student (name, surname, group_id) values (?,?,?)", students)

grades = [
    (1, 1, 4),
    (2, 2, 3),
    (3, 3, 5),
    (4, 1, 2),
    (5, 4, 5),
    (6, 5, 3)
]

cursor.executemany("insert into grade (student_id, lecture_id, grade) values (?,?,?)", grades)

conn.commit()
conn.close()
