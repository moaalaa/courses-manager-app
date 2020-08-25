import sqlite3


class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, course_name text, course_day text, course_duration text, course_price text)")
        self.connection.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM courses")
        return self.cursor.fetchall()

    def insert(self, course_name, course_day, course_duration, course_price):
        self.cursor.execute("INSERT INTO courses VALUES (NULL, ?, ?, ?, ?)", (course_name, course_day, course_duration, course_price))
        self.connection.commit()
    
    def remove(self, id):
        self.cursor.execute("DELETE FROM courses WHERE id = ?", (id,))
        self.connection.commit()
    
    def update(self, id, course_name, course_day, course_duration, course_price):
        self.cursor.execute("UPDATE courses SET course_name = ?, course_day = ?, course_duration = ?, course_price = ? WHERE id = ?", (course_name, course_day, course_duration, course_price, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
