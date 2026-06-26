import sqlite3 
db = sqlite3.connect("students.db")
cursor = db.cursor()

cursor.execute("""
INSERT INTO students VALUES (
    'Arya',
    'Python',
    100
   )
""")
db.commit()
print("Students Added!")
db.close()

import sqlite3

db = sqlite3.connect("students.db")
cursor = db.cursor()

cursor.execute("""
INSERT INTO students VALUES(
    'Alex',
    'Web Development',
    80
)
""")
db.commit ()
print("Student Added Successfully!")
db.close()

import sqlite3
db = sqlite3.connect("students.db")
cursor = db.cursor()
name = input("ENTER STUDENT NAME :")
course = input("ENTER COURSE NAME :")
progress = int(input("ENTER PROGRESS :"))
cursor.execute("""
    INSERT INTO students VALUES(?,?,?)
    """,(name,course,progress))

db.commit()
print("Students Added Successfully!")
db.close()

import sqlite3
db = sqlite3.connect("students.db")
cursor = db.cursor()
cursor.execute("""
    INSERT INTO students VALUES('Mia','Python',60)
    """)
cursor.execute ("""
    INSERT INTO students VALUES('Pooha','Wed Developer',90)
    """)
cursor.execute("""
    INSERT INTO students VALUES('Que','AI Learning',40)
    """)
db.commit()
print("Students Added Successfully")
db.close()

import sqlite3
db = sqlite3.connect("students.db")
cursor = db.cursor()
students = [
    ("Amit","Python",85),
    ("Anu","Web Develper",65),
    ("Liya","AI Learning",75),
]
cursor.executemany(
    "INSERT INTO students VALUES(?,?,?)",
    students
)
db.commit()
print("STUDENTS ADDED SUCCESSFULLY!")
db.close()
