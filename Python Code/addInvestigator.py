from tkinter import *


class AddInvestigator:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        main_font = "Arial 10"

        # Add Frame
        self.add_frame = Frame(width=50,
                               bg=background_color,
                               pady=10)
        self.add_frame.grid()

        # Add Heading (row 0)
        self.add_heading_label = Label(self.add_frame,
                                       text="Add Investigator",
                                       font="Arial 15 bold",
                                       bg=background_color,
                                       padx=50)
        self.add_heading_label.grid(row=0)

        # Last Name frame (row 1)
        self.last_frame = Frame(self.add_frame)
        self.last_frame.grid(row=1, pady=5, padx=30)

        self.lastname_label = Label(self.last_frame,
                                    font=main_font,
                                    text="Last Name",
                                    width=8,
                                    bg=background_color)
        self.lastname_label.grid(row=0, column=0)

        self.last_entry = Entry(self.last_frame,
                                width=15)
        self.last_entry.grid(row=0, column=1)

        # First Name frame (row 2)
        self.first_frame = Frame(self.add_frame)
        self.first_frame.grid(row=2, pady=0)

        self.first_label = Label(self.first_frame,
                                 font=main_font,
                                 text="First Name",
                                 width=8,
                                 bg=background_color)
        self.first_label.grid(row=1, column=0)

        self.pass_entry = Entry(self.first_frame,
                                width=15,
                                show="*")
        self.pass_entry.grid(row=1, column=1)

        # Button frame (row 3)
        self.button_frame = Frame(self.add_frame,
                                  bg=background_color)
        self.button_frame.grid(row=3, pady=10)

        self.close_button = Button(self.button_frame,
                                   text="Close",
                                   width=8,
                                   command=quit)
        self.close_button.grid(row=0, column=0, padx=5)

        self.login_button = Button(self.button_frame,
                                   text="Login",
                                   width=8)
        self.login_button.grid(row=0, column=1, padx=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("BD App")
    root.resizable(width=False, height=False)
    something = AddInvestigator(root)
    root.mainloop()
