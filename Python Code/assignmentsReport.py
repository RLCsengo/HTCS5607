from tkinter import *
import sqlite3
from tkinter.scrolledtext import ScrolledText
with sqlite3.connect("HTCS5607.db") as db:
    cursor = db.cursor()


class AssReport:
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
                                        text="Assignments Report",
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
        self.report_btn = Button(self.button_frame,
                                 width=15,
                                 height=2,
                                 text="Produce Report",
                                 command=self.show_ass_rep)
        self.report_btn.grid(row=0, column=1)

    def show_ass_rep(self):
        cursor.execute("SELECT * FROM ASSIGNMENT")
        for row in cursor.fetchall():
            case_id = ""
            case_id = row[1]
            inv_id = ""
            inv_id = row[2]
            hours = ""
            hours = row[3]
            cursor.execute("SELECT caseDescription FROM CASES WHERE CaseID=?", (case_id,))
            for row in cursor.fetchall():
                description = ""
                description = row[0]

            cursor.execute("SELECT lastName, firstName FROM INVESTIGATOR WHERE InvestigatorID=?", (inv_id,))
            for row in cursor.fetchall():
                lastName = ""
                lastName = row[0]
                firstName = ""
                firstName = row[1]

            line1 = "\nCase ID: {}         Description: {}         Hours: {}\n".format(case_id, description, hours)
            line2 = "Investigator ID: {}         Full Name: {}, {}\n\n\n".format(inv_id, lastName, firstName)
            line3 = "_________________________________________________\n\n\n"

            self.box.config(state=NORMAL)
            self.box.insert(INSERT, line1)
            self.box.insert(INSERT, line2)
            self.box.insert(INSERT, line3)
            continue


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Main Menu")
    root.resizable(width=False, height=False)
    something = AssReport(root)
    root.mainloop()
