import tkinter as tk

from classes.db import Database

# Connect to Database
db = Database('courses.db')

class Actions:
    @staticmethod
    def get_courses(container):
        print("Fetching Courses")
        
        container.delete(0, tk.END)
       
        rows = db.fetch()

        for row in rows:
            container.insert(tk.END, row)

    @staticmethod
    def add_course():
        print("Add Course")

    @staticmethod    
    def update_course():
        print("Update Course")
    
    @staticmethod
    def remove_course():
        print("Remove Course")

    @staticmethod
    def clear_fields():
        print("Clear Fields")
