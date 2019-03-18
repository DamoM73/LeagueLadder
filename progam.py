# This program keeps a track of the competitive games played at the MBBC Library
from tkinter import *
from PIL import Image, ImageTk

# Enter result window


# View ladders window


# View ranking window


# Resend code window


# Create competition window


# Add student window


# Edit results window

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

# title frame
frame_title = Frame(root, bg = "white")
frame_title.grid(row = 0, column = 0, padx = 10, pady = 10)

# button frame
frame_buttons = Frame(root, bg = "white")
frame_buttons.grid(row = 1, column = 0, padx = 10, pady = 50)

# create crest object
image = Image.open("crest.jpg")
crest = ImageTk.PhotoImage(image)

# place title in frame
Label(frame_title, image = crest, bd = 0)\
    .grid(row = 0, column = 0, rowspan = 2)
Label(frame_title, text = "Moreton Bay Boys' College", bg = "white", font=("Arial",20),fg="deep sky blue")\
    .grid(row = 0, column = 1, sticky = W)
Label(frame_title, text = "Competitive Games Leagues", bg = "white", font=("Arial",39),fg="deep sky blue")\
    .grid(row = 1, column = 1, sticky = W)

# place buttons in frame
# competition buttons
Label(frame_buttons, text = "Competitions", bg = "white", font=("Arial",17),fg = "deep sky blue")\
    .grid(row = 0, column = 0)

enter_result_btn = Button(frame_buttons, text = "Enter Results", width = 16, height = 2)
enter_result_btn.config(bg = "deep sky blue", fg = "white", bd = 0, font=("Arial",15))
enter_result_btn.grid(row = 1, column = 0, padx = 10, pady = 10)

view_ladders_btn = Button(frame_buttons, text = "View Ladders", width = 16, height = 2)
view_ladders_btn.config(bg = "deep sky blue", fg = "white", bd = 0, font=("Arial",15))
view_ladders_btn.grid(row = 2, column = 0, padx = 10, pady = 10)

# student buttons
Label(frame_buttons, text = "Students", bg = "white", font=("Arial", 17), fg = "DarkGoldenrod2")\
    .grid(row = 0, column = 1)

view_ranking_btn = Button(frame_buttons, text = "View Ranking", width = 16, height = 2)
view_ranking_btn.config(bg = "DarkGoldenrod2", fg = "white", bd = 0, font=("Arial",15))
view_ranking_btn.grid(row = 1, column = 1, padx = 10, pady = 10)

resend_code_btn = Button(frame_buttons, text = "Resend Code", width = 16, height = 2)
resend_code_btn.config(bg = "DarkGoldenrod2", fg = "white", bd = 0, font=("Arial",15))
resend_code_btn.grid(row = 2, column = 1, padx = 10, pady = 10)

# adminstration buttons
Label(frame_buttons, text = "Administration",bg = "white", font=("Arial",17),fg = "gray26")\
    .grid(row = 0, column = 2, columnspan = 2)

create_comp_btn = Button(frame_buttons, text = "Create Competition", width = 16, height = 2)
create_comp_btn.config(bg = "gray26", fg = "white", bd = 0, font=("Arial",15))
create_comp_btn.grid(row = 1, column = 2, padx = 10, pady = 10)

new_student_btn = Button(frame_buttons, text = "Add New Student", width = 16, height = 2)
new_student_btn.config(bg = "gray26", fg = "white", bd = 0, font=("Arial",15))
new_student_btn.grid(row = 2, column = 2, padx = 10, pady = 10)

edit_results_btn = Button(frame_buttons, text = "Edit Results", width = 16, height = 2)
edit_results_btn.config(bg = "gray26", fg = "white", bd = 0, font=("Arial",15))
edit_results_btn.grid(row = 1, column = 3, padx = 10, pady = 10)

# run mainloop
root.mainloop()
print("carry on now...")