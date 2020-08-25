import tkinter

from classes.actions import Actions

# Define our app
app = tkinter.Tk()

# Course Name
"""
To align items you should use sticky and it's keywords
N -> North -> Top
E -> East -> Right
W -> West -> Left
S -> South -> Down
and other compass directions
"""
course_label = tkinter.Label(app, text="Course Name", font=('bold', 14), padx=5, pady=20)
course_label.grid(row=0, column=0, sticky=tkinter.W)

course_name = tkinter.StringVar()
course_entry = tkinter.Entry(app, textvariable=course_name)
course_entry.grid(row=0, column=1, sticky=tkinter.WE)

# Course Day
course_day_label = tkinter.Label(app, text="Course Day", font=('bold', 14))
course_day_label.grid(row=0, column=2, sticky=tkinter.W)

course_day_name = tkinter.StringVar()
course_day_entry = tkinter.Entry(app, textvariable=course_day_name)
course_day_entry.grid(row=0, column=3)

# Course Duration
course_duration_label = tkinter.Label(app, text="Course Duration", font=('bold', 14), padx=5, pady=20)
course_duration_label.grid(row=1, column=0, sticky=tkinter.W)

course_duration_name = tkinter.StringVar()
course_duration_entry = tkinter.Entry(app, textvariable=course_duration_name)
course_duration_entry.grid(row=1, column=1)

# Course Price
course_price_label = tkinter.Label(app, text="Course Price", font=('bold', 14))
course_price_label.grid(row=1, column=2, sticky=tkinter.W)

course_price_name = tkinter.StringVar()
course_price_entry = tkinter.Entry(app, textvariable=course_price_name)
course_price_entry.grid(row=1, column=3)

# Buttons
add_button = tkinter.Button(app, text="Add Course", width=12, command=Actions.add_course)
add_button.grid(row=2, column=0, pady=20)

remove_button = tkinter.Button(app, text="Remove Course", width=12, command=Actions.remove_course)
remove_button.grid(row=2, column=1)

update_button = tkinter.Button(app, text="Update Course", width=12, command=Actions.update_course)
update_button.grid(row=2, column=2)

clear_button = tkinter.Button(app, text="Clear Fields", width=12, command=Actions.clear_fields)
clear_button.grid(row=2, column=3)

# Courses List
courses_lists = tkinter.Listbox(app, height=8, width=50, border=0)
courses_lists.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create Scrollbar
scroll_bar = tkinter.Scrollbar(app)
scroll_bar.grid(row=3, column=3)

# Set Scrollbar to Courses List
courses_lists.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=courses_lists.yview)

# Chanage main window title
app.title("Courses Manager")

# Change main window widthand height
app.geometry("700x350")

# Fetch Our Data
Actions.get_courses(courses_lists)

# Start our Program
app.mainloop()
