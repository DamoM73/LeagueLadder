# This program keeps a track of the competitive games played at the MBBC Library
from tkinter import *
from PIL import Image, ImageTk


# ENTER RESULTS WINDOW
def enter_result():
    # create window
    enter_result_wd = Toplevel()
    enter_result_wd.geometry(WINDOW_SIZE)
    enter_result_wd.title(TITLE + " - Enter Result")
    enter_result_wd.resizable(False, False)
    enter_result_wd.configure(bg = "white")

    # create frames
    title_fr = Frame(enter_result_wd, bg = "white")
    title_fr.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

    content_fr = Frame(enter_result_wd, bg = "white")
    content_fr.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10)

    # fill title frame
    Label(title_fr, image = crest, bd = 0)\
       .grid(row = 0, column = 0, rowspan = 2)
    Label(title_fr, text = "Moreton Bay Boys' College", bg = "white", font=("Arial",20),fg="deep sky blue")\
        .grid(row = 0, column = 1, sticky = W)
    Label(title_fr, text = "Enter Results", bg = "white", font=("Arial",39),fg="deep sky blue")\
        .grid(row = 1, column = 1, sticky = W)

# VIEW LADDERS WINDOW
def view_ladders():
    view_ladders_wd = Toplevel()
    view_ladders_wd.geometry(WINDOW_SIZE)
    view_ladders_wd.title(TITLE + " - View Ladders")
    view_ladders_wd.resizable(False, False)
    view_ladders_wd.configure(bg = "white")
    

# VIEW RANKING WINDOW
def view_ranking():
    view_ranking_wd = Toplevel()
    view_ranking_wd.geometry(WINDOW_SIZE)
    view_ranking_wd.title(TITLE + " - View Ranking")
    view_ranking_wd.resizable(False, False)
    view_ranking_wd.configure(bg = "white")


# RESEND CODE WINDOW
def resend_code():
    resend_code_wd = Toplevel()
    resend_code_wd.geometry(WINDOW_SIZE)
    resend_code_wd.title(TITLE + " - Resend Code")
    resend_code_wd.resizable(False, False)
    resend_code_wd.configure(bg = "white")


# CREATE COMPETITION WINDOW
def create_comp():
    create_comp_wd = Toplevel()
    create_comp_wd.geometry(WINDOW_SIZE)
    create_comp_wd.title(TITLE + " - Create Competition")
    create_comp_wd.resizable(False, False)
    create_comp_wd.configure(bg = "white")


# CREATE STUDENT WINDOW
def create_student():
    create_student_wd = Toplevel()
    create_student_wd.geometry(WINDOW_SIZE)
    create_student_wd.title(TITLE + " - Create New Student")
    create_student_wd.resizable(False, False)
    create_student_wd.configure(bg = "white")


# EDIT RESULTS WINDOW
def edit_results():
    edit_results_wd = Toplevel()
    edit_results_wd.geometry(WINDOW_SIZE)
    edit_results_wd.title(TITLE + " - Edit Results")
    edit_results_wd.resizable(False, False)
    edit_results_wd.configure(bg = "white")




# ---- MAIN PROGRAM ----

# Constants
WINDOW_SIZE = "830x550"
TITLE = "MBBC Competitive Games Leagues"


# MAIN WINDOW
# Create main window
root = Tk()
root.geometry(WINDOW_SIZE)
root.title(TITLE)
root.resizable(False, False)
root.configure(background = "white")

# create frames
main_title_fr = Frame(root, bg = "white")
main_title_fr.grid(row = 0, column = 0, padx = 10, pady = 10)

main_buttons_fr = Frame(root, bg = "white")
main_buttons_fr.grid(row = 1, column = 0, padx = 10, pady = 50)

# create crest object
image = Image.open("crest.jpg")
crest = ImageTk.PhotoImage(image)

# fill main_title frame
Label(main_title_fr, image = crest, bd = 0)\
    .grid(row = 0, column = 0, rowspan = 2)
Label(main_title_fr, text = "Moreton Bay Boys' College", bg = "white", font=("Arial",20),fg="deep sky blue")\
    .grid(row = 0, column = 1, sticky = W)
Label(main_title_fr, text = "Competitive Games Leagues", bg = "white", font=("Arial",39),fg="deep sky blue")\
    .grid(row = 1, column = 1, sticky = W)

# fill main_button frame
# competition buttons
Label(main_buttons_fr, text = "Competitions", bg = "white", font=("Arial",17),fg = "deep sky blue")\
    .grid(row = 0, column = 0)

# Enter results button
enter_result_btn = Button(main_buttons_fr, text = "Enter Results", width = 16, height = 2, command = enter_result)
enter_result_btn.config(bg = "deep sky blue", fg = "white", bd = 0, font=("Arial",15))
enter_result_btn.grid(row = 1, column = 0, padx = 10, pady = 10)

# View Ladders Button
view_ladders_btn = Button(main_buttons_fr, text = "View Ladders", width = 16, height = 2, command = view_ladders)
view_ladders_btn.config(bg = "deep sky blue", fg = "white", bd = 0, font=("Arial",15))
view_ladders_btn.grid(row = 2, column = 0, padx = 10, pady = 10)

# Student Buttons
Label(main_buttons_fr, text = "Students", bg = "white", font=("Arial", 17), fg = "DarkGoldenrod2")\
    .grid(row = 0, column = 1)

# View Rank Button
view_ranking_btn = Button(main_buttons_fr, text = "View Ranking", width = 16, height = 2, command = view_ranking)
view_ranking_btn.config(bg = "DarkGoldenrod2", fg = "white", bd = 0, font=("Arial",15))
view_ranking_btn.grid(row = 1, column = 1, padx = 10, pady = 10)

# Resend Code Button
resend_code_btn = Button(main_buttons_fr, text = "Resend Code", width = 16, height = 2, command = resend_code)
resend_code_btn.config(bg = "DarkGoldenrod2", fg = "white", bd = 0, font=("Arial",15))
resend_code_btn.grid(row = 2, column = 1, padx = 10, pady = 10)

# adminstration buttons
Label(main_buttons_fr, text = "Administration",bg = "white", font=("Arial",17),fg = "gray26")\
    .grid(row = 0, column = 2, columnspan = 2)

# Create Competition Button
create_comp_btn = Button(main_buttons_fr, text = "Create Competition", width = 16, height = 2, command = create_comp)
create_comp_btn.config(bg = "gray26", fg = "white", bd = 0, font=("Arial",15))
create_comp_btn.grid(row = 1, column = 2, padx = 10, pady = 10)

# Create New Student Button
new_student_btn = Button(main_buttons_fr, text = "Add New Student", width = 16, height = 2, command = create_student)
new_student_btn.config(bg = "gray26", fg = "white", bd = 0, font=("Arial",15))
new_student_btn.grid(row = 2, column = 2, padx = 10, pady = 10)

# Edit Results Button
edit_results_btn = Button(main_buttons_fr, text = "Edit Results", width = 16, height = 2, command = edit_results)
edit_results_btn.config(bg = "gray26", fg = "white", bd = 0, font=("Arial",15))
edit_results_btn.grid(row = 1, column = 3, padx = 10, pady = 10)

# run mainloop
root.mainloop()
print("carry on now...")