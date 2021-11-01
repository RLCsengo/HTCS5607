from tkinter import *


class Menu:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        username = "admin"

        # Login Frame
        self.menu_frame = Frame(width=50,
                                bg=background_color,
                                pady=10)
        self.menu_frame.grid()

        # Login Heading (row 0)
        self.menu_heading_label = Label(self.menu_frame,
                                        text="Main Menu",
                                        font="Arial 15 bold",
                                        bg=background_color,
                                        padx=50)
        self.menu_heading_label.grid(row=0)

        self.button_frame = Frame(self.menu_frame,
                                  bg=background_color)
        self.button_frame.grid(row=1, pady=10, padx=10)

        self.AddInv_button = Button(self.button_frame,
                                    text="Add Investigator",
                                    width=16)
        self.AddInv_button.grid(row=0, column=0, padx=2, pady=2)

        self.UptInv_button = Button(self.button_frame,
                                    text="Update Investigator",
                                    width=16)
        self.UptInv_button.grid(row=1, column=0, padx=2, pady=2)

        self.DelInv_button = Button(self.button_frame,
                                    text="Delete Investigator",
                                    width=16)
        self.DelInv_button.grid(row=2, column=0, padx=2, pady=2)

        self.InvRep_button = Button(self.button_frame,
                                    text="Produce Investigator\n"
                                         "Report",
                                    width=16)
        self.InvRep_button.grid(row=3, column=0, padx=2, pady=2)

        self.AssInv_button = Button(self.button_frame,
                                    text="Assign Investigator",
                                    width=16)
        self.AssInv_button.grid(row=0, column=1, padx=2, pady=2)

        self.RemInv_button = Button(self.button_frame,
                                    text="Remove Investigator",
                                    width=16)
        self.RemInv_button.grid(row=1, column=1, padx=2, pady=2)

        self.CloCas_button = Button(self.button_frame,
                                    text="Close Case",
                                    width=16)
        self.CloCas_button.grid(row=2, column=1, padx=2, pady=2)

        self.AssRep_button = Button(self.button_frame,
                                    text="Produce Assignments\n"
                                         "Report",
                                    width=16)
        self.AssRep_button.grid(row=3, column=1, padx=2, pady=2)

        self.close_button = Button(self.button_frame,
                                   text="Close",
                                   width=16,
                                   command=quit)
        self.close_button.grid(row=4, column=0, padx=5, pady=15)

        if username == "payroll":
            self.AssInv_button.config(state=DISABLED)
            self.RemInv_button.config(state=DISABLED)
            self.CloCas_button.config(state=DISABLED)
            self.AssRep_button.config(state=DISABLED)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Main Menu")
    root.resizable(width=False, height=False)
    something = Menu(root)
    root.mainloop()
