# Importing tkinter module
from tkinter import *
import random
# Importing calendar module
import calendar

# Function to show calendar of the given year
def showCalendar():
    gui = Tk()
    gui.config(background=random.choice(bg_colors))
    gui.title("Calendar for the year")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold", justify=LEFT)
    calYear.pack(pady=10, padx=10, fill=BOTH, expand=True)
    gui.mainloop()

# Driver code
if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")

    # configure grid rows and columns to resize automatically
    new.grid_columnconfigure(0, weight=1)
    new.grid_rowconfigure(0, weight=1)
    new.grid_rowconfigure(1, weight=1)
    new.grid_rowconfigure(2, weight=1)
    new.grid_rowconfigure(3, weight=1)

    # set background color options
    bg_colors = ["red", "blue", "green", "yellow", "purple"]

    # get screen size
    screen_width = new.winfo_screenwidth()
    screen_height = new.winfo_screenheight()

    # set size of the window
    new_width = screen_width // 3
    new_height = screen_height // 3
    new.geometry(f"{new_width}x{new_height}")

    cal = Label(new, text="Calendar",bg='grey',font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calendar', fg='Black', bg='Blue', command=showCalendar)

    # place widgets on the grid
    cal.grid(row=0, column=0, pady=10)
    year.grid(row=1, column=0, padx=10, pady=10)
    year_field.grid(row=2, column=0, padx=10, pady=10)
    button.grid(row=3, column=0, pady=10)

    new.mainloop()
