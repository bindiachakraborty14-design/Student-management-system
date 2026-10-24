import sqlite3

def get_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_student(name, age, course, email):
    conn = get_connection()

    conn.execute(
        "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
        (name, age, course, email)
    )

    conn.commit()
    conn.close()



def get_students():
    conn = get_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()
    print(type(students[0])) if students else print("No students found")

    conn.close()
    return students


def get_student(student_id):
    conn = get_connection()

    student = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    conn.close()
    return student


def update_student(student_id, name, age, course, email):
    conn = get_connection()

    conn.execute(
        """
        UPDATE students
        SET name = ?, age = ?, course = ?, email = ?
        WHERE id = ?
        """,
        (name, age, course, email, student_id)
    )

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()