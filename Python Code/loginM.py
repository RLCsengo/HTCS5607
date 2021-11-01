from tkinter import *
from threading import Timer


class Login:
    def __init__(self, parent):
        # Formatting Variables
        background_color = "#E3EBF8"
        main_font = "Arial 10"

        # Login Frame
        self.login_frame = Frame(width=50,
                                 bg=background_color,
                                 pady=10)
        self.login_frame.grid()

        # Login Heading (row 0)
        self.login_heading_label = Label(self.login_frame,
                                         text="Login",
                                         font="Arial 15 bold",
                                         bg=background_color,
                                         padx=10)
        self.login_heading_label.grid(row=0)

        # User frame (row 1)
        self.user_frame = Frame(self.login_frame)
        self.user_frame.grid(row=1, pady=5, padx=30)

        self.username_label = Label(self.user_frame,
                                    font=main_font,
                                    text="Username",
                                    width=8,
                                    bg=background_color)
        self.username_label.grid(row=0, column=0)

        self.user_entry = Entry(self.user_frame,
                                width=15)
        self.user_entry.grid(row=0, column=1)

        # Pass frame (row 2)
        self.pass_frame = Frame(self.login_frame)
        self.pass_frame.grid(row=2, pady=0)

        self.pass_label = Label(self.pass_frame,
                                font=main_font,
                                text="Password",
                                width=8,
                                bg=background_color)
        self.pass_label.grid(row=1, column=0)

        self.pass_entry = Entry(self.pass_frame,
                                width=15,
                                show="*")
        self.pass_entry.grid(row=1, column=1)

        # Button frame (row 3)
        self.button_frame = Frame(self.login_frame,
                                  bg=background_color)
        self.button_frame.grid(row=3, pady=10)

        self.close_button = Button(self.button_frame,
                                   text="Close",
                                   width=8,
                                   command=quit)
        self.close_button.grid(row=0, column=0, padx=5)

        self.login_button = Button(self.button_frame,
                                   text="Login",
                                   width=8,
                                   command=self.check_login)
        self.login_button.grid(row=0, column=1, padx=5)

    def check_login(self):
        self.user_entry.config(bg="white")
        self.pass_entry.config(bg="white")
        # checks answer and configures buttons based on whether or not the answer was correct
        try:
            user_input = self.user_entry.get()
            pass_input = self.pass_entry.get()

            if user_input == "payroll":
                if pass_input == "5545":
                    username = user_input
                    self.login_heading_label.config(text="Logging in...")
                    self.close_button.config(state="disabled")
                    self.login_button.config(state="disabled")
                    self.user_entry.config(state="disabled")
                    self.pass_entry.config(state="disabled")
                    # t = Timer(3.0, to_menu)
                else:
                    self.login_heading_label.config(text="Wrong Password")
                    self.pass_entry.config(bg="#FF0000")
                    self.pass_entry.delete(0, 'end')

            elif user_input == "admin":
                if pass_input == "4454":
                    username = user_input
                    self.login_heading_label.config(text="Logging in...")
                    self.close_button.config(state="disabled")
                    self.login_button.config(state="disabled")
                    self.user_entry.config(state="disabled")
                    self.pass_entry.config(state="disabled")
                    # t = Timer(3.0, to_menu)
                else:
                    self.login_heading_label.config(text="Wrong Password")
                    self.pass_entry.delete(0, 'end')
                    self.pass_entry.config(bg="#FF0000")

            else:
                self.login_heading_label.config(text="Wrong Username")
                self.user_entry.config(bg="#FF0000")
                self.user_entry.delete(0, 'end')
                self.pass_entry.delete(0, 'end')

        except ValueError:
            print("ERROR")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Login")
    root.resizable(width=False, height=False)
    something = Login(root)
    root.mainloop()
