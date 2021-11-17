from tkinter import *
from tkinter.scrolledtext import ScrolledText


class Menu:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"

        # Login Frame
        self.menu_frame = Frame(width=50,
                                bg=background_color,
                                pady=10)
        self.menu_frame.grid()

        # Login Heading (row 0)
        self.menu_heading_label = Label(self.menu_frame,
                                        text="Investigator Report",
                                        font="Arial 15 bold",
                                        bg=background_color,
                                        padx=150,
                                        pady=10)
        self.menu_heading_label.grid(row=0)

        self.box = ScrolledText(self.menu_frame,
                                width=100,
                                height=30)
        self.box.grid(row=1)

        self.button_frame = Frame(self.menu_frame)
        self.button_frame.grid(row=2)

        self.return_btn = Button(self.button_frame,
                                 width=15,
                                 height=2,
                                 text="Return")
        self.return_btn.grid(row=0)
        self.produce_btn = Button(self.button_frame,
                                  width=15,
                                  height=2,
                                  text="Produce Report")
        self.produce_btn.grid(row=0, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Main Menu")
    root.resizable(width=False, height=False)
    something = Menu(root)
    root.mainloop()
