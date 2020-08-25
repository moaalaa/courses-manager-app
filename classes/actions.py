import tkinter as tk
from tkinter import messagebox

from classes.db import Database

# Connect to Database
db = Database('courses.db')

class Actions:
    COURSE_ID = None
    CONTAINER = None

    @staticmethod
    def get_courses():
        print("Fetching Courses")
        
        Actions.CONTAINER.delete(0, tk.END)
       
        rows = db.fetch()

        for row in rows:
            Actions.CONTAINER.insert(tk.END, row)

    @staticmethod
    def add_course(course_name, course_day, course_duration, course_price):
        error = False
        if course_name == '':
            error = True

        if course_day == '':
            error = True
            
        if course_duration == '':
            error = True
        
        if course_price == '':
            error = True
            
        if error:
            messagebox.showerror("No Data Found", "Please Fill All Fields Data")
            return

        print("Add Course")
        db.insert(course_name, course_day, course_duration, course_price)
        Actions.get_courses()

    @staticmethod    
    def update_course(course_name, course_day, course_duration, course_price):
        error = False
        if course_name == '':
            error = True

        if course_day == '':
            error = True
            
        if course_duration == '':
            error = True
        
        if course_price == '':
            error = True
            
        if error:
            messagebox.showerror("No Data Found", "Please Fill All Fields Data")
            return

        print("Update Course")
        db.update(Actions.COURSE_ID, course_name, course_day, course_duration, course_price)
        Actions.get_courses()
    
    @staticmethod
    def remove_course():
        db.remove(Actions.COURSE_ID)
        Actions.get_courses()
