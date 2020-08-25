import tkinter

from classes.actions import Actions


def clear_fields():
    course_entry.delete(0, tkinter.END)
    course_day_entry.delete(0, tkinter.END)
    course_duration_entry.delete(0, tkinter.END)
    course_price_entry.delete(0, tkinter.END)

def select_course_item(event):
    index = Actions.CONTAINER.curselection()[0]
    selected_item = Actions.CONTAINER.get(index)
    
    clear_fields()
    
    course_entry.insert(tkinter.END, selected_item[1])
    course_day_entry.insert(tkinter.END, selected_item[2])
    course_duration_entry.insert(tkinter.END, selected_item[3])
    course_price_entry.insert(tkinter.END, selected_item[4])
    
    Actions.COURSE_ID = selected_item[0]


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
course_entry.grid(row=0, column=1)

# Course Day
course_day_label = tkinter.Label(app, text="Course Day", font=('bold', 14))
course_day_label.grid(row=0, column=2, sticky=tkinter.W)

course_day = tkinter.StringVar()
course_day_entry = tkinter.Entry(app, textvariable=course_day)
course_day_entry.grid(row=0, column=3)

# Course Duration
course_duration_label = tkinter.Label(app, text="Course Duration", font=('bold', 14), padx=5, pady=20)
course_duration_label.grid(row=1, column=0, sticky=tkinter.W)

course_duration = tkinter.StringVar()
course_duration_entry = tkinter.Entry(app, textvariable=course_duration)
course_duration_entry.grid(row=1, column=1)

# Course Price
course_price_label = tkinter.Label(app, text="Course Price", font=('bold', 14))
course_price_label.grid(row=1, column=2, sticky=tkinter.W)

course_price = tkinter.StringVar()
course_price_entry = tkinter.Entry(app, textvariable=course_price)
course_price_entry.grid(row=1, column=3)

# Buttons
add_button = tkinter.Button(
    app, 
    text="Add Course", 
    width=12, 
    command=lambda: Actions.add_course(
        course_name.get(), 
        course_day.get(), 
        course_duration.get(), 
        course_price.get(), 
    )
)

add_button.grid(row=2, column=0, pady=20)

remove_button = tkinter.Button(app, text="Remove Course", width=12, command=lambda: [Actions.remove_course(), clear_fields()])
remove_button.grid(row=2, column=1)

update_button = tkinter.Button(
    app, 
    text="Update Course", 
    width=12, 
    command=lambda: Actions.update_course(
        course_name.get(), 
        course_day.get(), 
        course_duration.get(), 
        course_price.get(), 
    )
)
update_button.grid(row=2, column=2)

clear_button = tkinter.Button(app, text="Clear Fields", width=12, command=clear_fields)
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

# Bind courses list select event
courses_lists.bind("<<ListboxSelect>>", select_course_item)

# Chanage main window title
app.title("Courses Manager")

# Change main window widthand height
app.geometry("700x350")

# Change Main logo
app.wm_iconbitmap('./logo.ico')

# Fetch Our Data
Actions.CONTAINER = courses_lists
Actions.get_courses()

# Start our Program
app.mainloop()
