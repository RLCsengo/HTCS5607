from tkinter import *
import sqlite3
from tkinter.scrolledtext import ScrolledText
with sqlite3.connect("HTCS5607.db") as db:
    cursor = db.cursor()


class InvReport:
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
                                  text="Produce Report",
                                  command=self.show_rep)
        self.produce_btn.grid(row=0, column=1)

    def show_rep(self):
        cursor.execute("SELECT * FROM INVESTIGATOR")
        for row in cursor.fetchall():
            inv_id = ""
            inv_id = row[0]
            inv_last = ""
            inv_last = row[1]
            inv_first = ""
            inv_first = row[2]
            inv_rate = ""
            inv_rate = row[3]
            inv_street = ""
            inv_street = row[4]
            inv_suburb = ""
            inv_suburb = row[5]
            inv_num = ""
            inv_num = row[6]
            line1 = "\nID: {}         Full Name: {}, {}\n".format(inv_id, inv_last, inv_first)
            line2 = "Phone Number: {}         Street Address: {}, {}\n".format(inv_num, inv_street, inv_suburb)
            cases = 0
            cursor.execute("SELECT AssignmentID FROM ASSIGNMENT WHERE InvestigatorID=?",(inv_id,))
            for row in cursor.fetchall():
                cases = cases+1
            line3 = "Number of cases assigned: {}\n\n\n".format(cases)
            line4 = "_________________________________________________\n\n\n"

            self.box.config(state=NORMAL)
            self.box.insert(INSERT, line1)
            self.box.insert(INSERT, line2)
            self.box.insert(INSERT, line3)
            self.box.insert(INSERT, line4)

            continue


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Main Menu")
    root.resizable(width=False, height=False)
    something = InvReport(root)
    root.mainloop()
